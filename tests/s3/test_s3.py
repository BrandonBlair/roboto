import json

from roboto.s3.models.s3_responses import S3PutResponse


class S3Tests:
    def test_can_put_and_get_objects(self, s3_bucket):
        objects = s3_bucket.list_objects()
        assert objects == []

        desired_key = 'mykey'
        data = json.dumps(
            {
                "some_key": "some_value"
            }
        )
        put_resp = s3_bucket.put_object(
            bucket_name=s3_bucket.name,
            key=desired_key,
            body=data
        )

        assert isinstance(put_resp, S3PutResponse)
