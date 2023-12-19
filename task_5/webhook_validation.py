import hashlib
import hmac


def generate_hash_signature(
        secret: bytes,
        payload: bytes,
        digest_method=hashlib.sha1
):
    return hmac.new(secret, payload, digest_method).hexdigest()
