import json

from roboto.kinesis.models.responses import PutRecordResponse


class KinesisTests:
    def test_can_put_and_get_record(self, kinesis_stream):
        mock_dict = {'test_key': 'test_value'}
        mock_data = json.dumps(mock_dict)
        mock_part_key = 'test'

        put_resp = kinesis_stream.put_record(
            data=mock_data,
            part_key=mock_part_key
        )
        assert isinstance(put_resp, PutRecordResponse)

        assert put_resp.shard_id is not None
        assert put_resp.sequence_number is not None
        assert put_resp.encryption_type is None

        shard_ids = [s.id for s in kinesis_stream.info.shards]
        desired_shard = shard_ids[0]
        record_resp = kinesis_stream.get_records(shard_id=desired_shard)
        assert record_resp.records == []
