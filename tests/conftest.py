from boto.kinesis import connect_to_region
from moto import mock_kinesis, mock_s3

from pytest import fixture
from roboto.kinesis import KinesisStream
from roboto.s3 import S3Bucket


@fixture(scope='function')
def kinesis_stream():
    with mock_kinesis():
        stream_name = 'unimportant'
        kinesis = KinesisStream(name=stream_name)

        # Create mocked stream via moto
        kinesis.client.create_stream(StreamName=stream_name, ShardCount=2)

        yield kinesis

@fixture(scope='function')
def s3_bucket():
    with mock_s3():
        bucket_name = 'unimportant'
        s3 = S3Bucket(name=bucket_name)
        s3.client.create_bucket(Bucket=bucket_name)
        yield s3
