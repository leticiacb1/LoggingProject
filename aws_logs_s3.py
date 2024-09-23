import io
import logging

from dataclass.bucket import Bucket

username = "leticiacb1"

bucket_name = "log-bucket-2-" + username
key = "log1"

# Create Bucket:
s3 = Bucket()
s3.create(bucket_name = bucket_name)

# Logs:
log = logging.getLogger("my_logger")
string_io = io.StringIO()
handler = logging.StreamHandler(string_io)
log.addHandler(handler)

try:
    # Simulate exception
    raise ValueError
except ValueError:
    log.error("Missing value")
    log.error("Some error occurred!")
finally:
    # Persists logs to s3
    body = string_io.getvalue()
    s3.write_logs(body=body, bucket=bucket_name, key=key)
    s3.cleanup(bucket_name=bucket_name, key=key)