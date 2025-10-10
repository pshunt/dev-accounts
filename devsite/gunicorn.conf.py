# bind = "0.0.0.0:8000"
# workers = 3
# timeout = 30
# max_requests = 1000
# max_requests_jitter = 100
# accesslog = "-"
# errorlog = "-"

import os

bind = f"0.0.0.0:{os.getenv('PORT', '8000')}"  # default 8000 locally; Render sets $PORT
workers = int(os.getenv("WEB_CONCURRENCY", "3"))
accesslog = "-"
errorlog = "-"
timeout = 30
max_requests = 1000
max_requests_jitter = 100