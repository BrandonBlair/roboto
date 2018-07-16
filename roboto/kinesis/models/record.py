import json

from roboto.boto_response import BotoResponse


class Record(BotoResponse):
    def __init__(self, **record_map):
        super().__init__(**record_map)
        self.sequence_number = record_map.get('SequenceNumber')
        self.approximate_arrival_timestamp = record_map.get('ApproximateArrivalTimestamp')
        self.data_bytes = record_map.get('Data')

    @property
    def data(self):
        data_dict = json.loads(self.data_bytes)
        return data_dict
