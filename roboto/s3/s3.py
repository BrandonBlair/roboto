from boto3 import client

from .models.s3_bucket_object import S3BucketObject, S3BucketList
from .models.s3_responses import S3PutResponse


class S3Bucket(object):
    """AWS S3 Bucket represented as an object with customizable and readable methods"""

    def __init__(self, name):
        self.name = name
        self.client = client('s3')

    def put_object(self, bucket_name, key, body=None):
        """Put an object into an S3 bucket"""

        kw = {
            'Bucket': bucket_name,
            'Key': key,
        }
        if body:
            kw['Body'] = body

        put_resp = self.client.put_object(**kw)
        return S3PutResponse(**put_resp)

    def get_object(self, key):
        """Retrieve an object from the S3 bucket using its key"""

        object_data = self.client.get_object(
            Bucket=self.name,
            Key=key,
        )
        return S3BucketObject(**object_data)

    def list_objects(self, max_keys=100, prefix='', start_after=''):
        """List objects in an S3 bucket, limited by `max_keys`"""

        bucket_obj_map = self.client.list_objects_v2(
            Bucket=self.name,
            MaxKeys=max_keys,
            Prefix=prefix,
            StartAfter=start_after
        )
        bucket_obj_list = S3BucketList(**bucket_obj_map)

        return bucket_obj_list.contents

    @property
    def keys(self):
        """List of keys (limit 10000) for objects in S3 bucket"""

        _keys = [obj.key for obj in self.list_objects(max_keys=10000)]
        return _keys
