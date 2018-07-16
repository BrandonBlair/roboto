from .shard import Shard
from .record import Record

from roboto.boto_response import BotoResponse


class PutRecordResponse(BotoResponse):
    def __init__(self, **record_response):
        """Object describing the boto3 response for a put_record action

        Args:
            boto_response (dict): put_record response from boto
        """

        super().__init__(**record_response)
        self.shard_id = record_response.get('ShardId')
        self.sequence_number = record_response.get('SequenceNumber')
        self.encryption_type = record_response.get('EncryptionType')


class StreamSummary(BotoResponse):
    def __init__(self, **summary_resp):
        """Object describing the boto3 response for a describe_stream_summary action

        Args:
            summary_resp (dict): describe_stream_summary response from boto
        """

        super().__init__(**summary_resp)

        self.name = summary_resp.get('StreamName')
        self.arn = summary_resp.get('StreamArn')
        self.status = summary_resp.get('StreamStatus')
        self.retention_period_hours = summary_resp.get('RetentionPeriodHours')
        self.creation_timestamp = summary_resp.get('StreamCreationTimestamp')
        self.enhanced_monitoring = summary_resp.get('EnhancedMonitoring')
        self.encryption_type = summary_resp.get('EncryptionType')
        self.key_id = summary_resp.get('KeyId')

        # Only present on full description
        self.open_shard_count = summary_resp.get('OpenShardCount')


class StreamDescription(StreamSummary):
    def __init__(self, **description_resp):
        """Object describing the boto3 response for a describe_stream action

        Args:
            description_resp (dict): describe_stream response from boto
        """

        super().__init__(**description_resp)

        _shards = [
            Shard(**shard_map) for shard_map in description_resp.get('Shards')
        ]

        self.shards = _shards
        self.has_more_shards = description_resp.get('HasMoreShards')


class StreamRecords(BotoResponse):
    def __init__(self, **records_response):
        """Object describing the boto3 response for retrieving record_response

        Args:
            record_response (dict): get_records response from boto
        """

        super().__init__(**records_response)

        _records = [
            Record(**record_map) for record_map in records_response.get('Records')
        ]

        self.records = _records
        self.next_shard_iterator = records_response.get('NextShardIterator')
        self.millis_behind_latest = records_response.get('MillisBehindLatest')
