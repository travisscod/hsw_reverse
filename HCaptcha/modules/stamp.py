import hashlib
import base64
import os
import time
from datetime import datetime, timedelta

class HashcashPOW:
    def __init__(self, bits, salt_len=8, extra=""):
        self.bits = bits
        self.zeros = bits // 4
        self.salt_len = salt_len
        self.extra = extra

    def mint(self, resource):
        version = "1"
        salt = self._get_salt()
        date = datetime.utcnow().strftime("%Y-%m-%d")
        counter = 0

        while True:
            stamp = f"{version}:{self.bits//2}:{date}:{resource}:{self.extra}:{salt}:{counter}"
            if self._check_zeros(stamp):
                return stamp
            counter += 1

    def check(self, stamp):
        if self._check_date(stamp):
            return self._check_zeros(stamp)
        return False

    def _get_salt(self):
        salt = base64.urlsafe_b64encode(os.urandom(self.salt_len)).decode('utf-8')
        return salt[:self.salt_len]

    def _check_zeros(self, stamp):
        hashed_stamp = hashlib.sha1(stamp.encode()).digest()
        first_byte = hashed_stamp[0]
        bits = 8 - (self.bits // 4)
        return first_byte >> bits == 0

    def _check_date(self, stamp):
        fields = stamp.split(":")
        if len(fields) != 7:
            return False
        then = datetime.strptime(fields[2], "%Y-%m-%d")
        duration = datetime.utcnow() - then
        return duration.days * 24 <= 48

def get_stamp(difficulty, data):
    hasher = HashcashPOW(difficulty * 2)
    return hasher.mint(data)


