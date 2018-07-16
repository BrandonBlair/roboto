from roboto.boto_response import BotoResponse


class Shard(BotoResponse):
    def __init__(self, **shard_map):
        super().__init__(**shard_map)
        self.id = shard_map.get('ShardId')
        self.parent_id = shard_map.get('ParentShardId')
        self.adjacent_parent_id = shard_map.get('AdjacentParentShardId')
        self.hash_key_range = shard_map.get('HashKeyRange')
        self.sequence_number_range = shard_map.get('SequenceNumberRange')
