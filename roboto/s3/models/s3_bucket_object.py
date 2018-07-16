from roboto.boto_response import BotoResponse


class S3BucketList(BotoResponse):
    def __init__(self, **obj_resp_map):
        super().__init__(**obj_resp_map)
        self.is_truncated = obj_resp_map.get('IsTruncated', False)
        contents = obj_resp_map.get('Contents')
        self.contents = [S3BucketObjectEntry(**items) for items in contents] if contents else []
        self.name = obj_resp_map.get('Name')
        self.prefix = obj_resp_map.get('Prefix')
        self.delimiter = obj_resp_map.get('Delimiter')
        self.max_keys = obj_resp_map.get('MaxKeys')
        self.common_prefixes = obj_resp_map.get('CommonPrefixes')
        self.encoding_type = obj_resp_map.get('EncodingType')
        self.key_count = obj_resp_map.get('KeyCount')
        self.continuation_token = obj_resp_map.get('ContinuationToken')
        self.next_continuation_token = obj_resp_map.get('NextContinuationToken')
        self.start_after = obj_resp_map.get('StartAfter')


class S3BucketObjectEntry(BotoResponse):
    def __init__(self, **contents_map):
        super().__init__(**contents_map)
        self.key = contents_map.get('Key')
        self.last_modified = contents_map.get('LastModified')
        self.etag = contents_map.get('ETag')
        self.size = contents_map.get('Size')
        self.storage_class = contents_map.get('StorageClass')
        self.owner = contents_map.get('Owner')


class S3BucketObject(BotoResponse):
    def __init__(self, **object_data):
        super().__init__(**object_data)
        self.body = object_data.get('Body')
        self.delete_marker = object_data.get('DeleteMarker')
        self.accept_ranges = object_data.get('AcceptRanges')
        self.expiration = object_data.get('Expiration')
        self.restore = object_data.get('Restore')
        self.last_modified = object_data.get('LastModified')
        self.content_length = object_data.get('ContentLength')
        self.etag = object_data.get('ETag')
        self.missing_meta = object_data.get('MissingMeta')
        self.version_id = object_data.get('VersionId')
        self.cache_control = object_data.get('CacheControl')
        self.content_disposition = object_data.get('ContentDisposition')
        self.content_encoding = object_data.get('ContentEncoding')
        self.content_language = object_data.get('ContentLanguage')
        self.content_range = object_data.get('ContentRange')
        self.content_type = object_data.get('ContentType')
        self.expires = object_data.get('Expires')
        self.website_redirection_location = object_data.get('WebsiteRedirectionData')
        self.server_side_encryption = object_data.get('ServerSideEncryption')
        self.metadata = object_data.get('Metadata')
        self.sse_customer_algorithm = object_data.get('SSECustomerAlgorithm')
        self.sse_customer_key_md5 = object_data.get('SSECustomerKeyMD5')
        self.sse_kms_key_id = object_data.get('SSEKMSKeyID')
        self.storage_class = object_data.get('StorageClass')
        self.request_charged = object_data.get('RequestCharged')
        self.replication_status = object_data.get('ReplicationStatus')
        self.parts_count = object_data.get('PartsCount')
        self.tag_count = object_data.get('TagCount')
