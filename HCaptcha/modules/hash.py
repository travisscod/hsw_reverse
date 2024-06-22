import xxhash
import random
import zlib


def rand_hash(input_bytes):
    crc = zlib.crc32(input_bytes) & 0xFFFFFFFF
    hash_value = crc * 2.3283064365386963e-10
    return crc, hash_value

def hash(data: str) -> str:
    return xxhash.xxh64_intdigest(data, seed=5575352424011909552)

def random_hash(len: int) -> str:
    return "".join(random.choices("0123456789", k=len))

