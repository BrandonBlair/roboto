from boto3 import client

from .models.responses import PutRecordResponse, StreamDescription, StreamSummary, StreamRecords
from .exceptions import KinesisException


class KinesisStream(object):
    """AWS Kinesis Stream represented as an object with customizable and expressive methods"""

    def __init__(self, name):
        self.name = name
        self.client = client('kinesis')

    def put_record(self, data, part_key):
        """Adds a single record to a Kinesis stream

        Args:
            stream_name (str): Name of stream to which we want to add a record
            data (bytes): Data blob serialized using base64 encoding
            part_key (str): Which shard will receive the record (partition key)
            hash_key (str): Overrides partition key to determine which shard record belongs to
            seq_num (str): Should be set to the sequence number of the previously added record.
                           If not provided, a coarse arrival time is used.
        """

        response_map = self.client.put_record(
            StreamName=self.name,
            Data=data,
            PartitionKey=part_key,
        )

        record_response = PutRecordResponse(**response_map)

        return record_response

    @property
    def info(self):
        """Info describing a particular kinesis stream."""

        response_map = self.client.describe_stream(
            StreamName=self.name,
            Limit=100,
        ).get('StreamDescription')

        description = StreamDescription(**response_map)
        return description

    @property
    def summary(self):
        """Summary of kinesis stream info excluding shard data"""

        response_map = self.client.describe_stream_summary(
            StreamName=self.name,
        ).get('StreamDescriptionSummary')

        description = StreamSummary(**response_map)
        return description

    def get_records(self, shard_id=None, shard_iterator=None, limit=100):
        """Records retrieved from the Kinesis stream"""

        if shard_id is None and shard_iterator is None:
            raise KinesisException('must provide shard_id or shard_iterator')

        shard_iterator = shard_iterator or self.get_shard_iterator(shard_id)

        records_response = self.client.get_records(
            ShardIterator=shard_iterator,
            Limit=limit
        )
        records = StreamRecords(**records_response)
        return records

    def get_shard_iterator(self, shard_id, iter_type='LATEST', timestamp=None):
        """Retrieves shard iterator

        Available iter_types:
            AT_SEQUENCE_NUMBER
            AFTER_SEQUENCE_NUMBER
            AT_TIMESTAMP
            TRIM_HORIZON
            LATEST
        """

        _kwargs = {
            "StreamName": self.name,
            "ShardId": shard_id,
            "ShardIteratorType": iter_type
        }

        if timestamp:
            _kwargs["Timestamp"] = timestamp

        response = self.client.get_shard_iterator(**_kwargs)

        shard_iterator = response.get('ShardIterator')
        return shard_iterator
