from setuptools import setup, find_packages

setup(
    name='roboto',
    version="1.0.4",
    summary="Readable, expressive, object-oriented approach to common Amazon Web Services",
    description="README.md",
    author="Brandon Blair",
    author_email="cbrandon.blair@gmail.com",
    packages=find_packages(),
    install_requires=[
        "boto3>=1.7.26",
    ]
)