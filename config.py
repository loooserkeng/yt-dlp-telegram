import os

token = os.environ["BOT_TOKEN"]

whitelist = None
blacklist = None
logs = None

max_filesize = 50000000
max_cookie_filesize = 1000000

max_user_concurrent_downloads = 1
max_global_concurrent_downloads = 2

max_retries = 3
retry_delay = 5

output_folder = "/tmp/satoru"

allowed_domains = [
    "youtube.com",
    "www.youtube.com",
    "youtu.be",
    "m.youtube.com",
    "youtube-nocookie.com",

    "tiktok.com",
    "www.tiktok.com",
    "vm.tiktok.com",
    "vt.tiktok.com",

    "instagram.com",
    "www.instagram.com",

    "twitter.com",
    "www.twitter.com",

    "x.com",
    "www.x.com",

    "bsky.app",
    "www.bsky.app",
]

allowed_image_domains = None

secret_key = os.environ.get(
    "SECRET_KEY",
    "change-this-secret-key"
)

js_runtime = {
    "bun": {
        "path": "bun"
    }
}

forward_to = None
forward_permissions = []
