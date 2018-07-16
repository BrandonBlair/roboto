class BotoResponse(object):
    """Provides the underlying dict when boto3 response is treated as a string"""

    def __init__(self, **response_map):
        self._data_map = response_map

    def __str__(self):
        return f"{self._data_map}"
