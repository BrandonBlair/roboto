from roboto.boto_response import BotoResponse


class Record(BotoResponse):
    def __init__(self, **record_map):
        super().__init__(**record_map)
        self.sequence_number = record_map.get('SequenceNumber')
        self.approximate_arrival_timestamp = record_map.get('ApproximateArrivalTimestamp')
        self.data = record_map.get('Data')
        self.partition_key.get('PartitionKey')
        self.encryption_type.get('EncryptionType')
