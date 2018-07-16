from roboto.boto_response import BotoResponse


class S3PutResponse(BotoResponse):
    def __init__(self, **obj_resp_map):
        super().__init__(**obj_resp_map)
        self.expiration = obj_resp_map.get('Expiration')
        self.etag = obj_resp_map.get('ETag')
        self.server_side_encryption = obj_resp_map.get('ServerSideEncryption')
        self.version_id = obj_resp_map.get('VersionId')
        self.sse_customer_algorithm = obj_resp_map.get('SSECustomerAlgorithm')
        self.sse_customer_key_md5 = obj_resp_map.get('SSECustomerKeyMD5')
        self.sse_kms_key_id = obj_resp_map.get('SSEKMSKeyId')
        self.request_charged = obj_resp_map.get('RequestCharged')
