from pytube import YouTube
from pytube.innertube import _default_clients

_default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID_CREATOR"]
YouTube('https://www.youtube.com/shorts/YulstVeLi7g',
        use_oauth=True,
        allow_oauth_cache=True
        ).streams.first().download()
