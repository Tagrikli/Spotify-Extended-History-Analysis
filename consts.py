

class AUDIO_FIELD:
    TIMESTAMP = 'ts'
    PLATFORM = 'platform'
    MS_PLAYED = 'ms_played'
    CONN_COUNTRY = 'conn_country'
    TRACK_NAME = 'master_metadata_track_name'
    ALBUM_NAME = 'master_metadata_album_album_name'
    ARTIST_NAME = 'master_metadata_album_artist_name'
    SPOTIFY_TRACK_URI = 'spotify_track_uri'
    EPISODE_NAME = 'episode_name'
    EPISODE_SHOW_NAME = 'episode_show_name'
    REASON_START = 'reason_start'
    REASON_END = 'reason_end'
    SHUFFLE = 'shuffle'
    SKIPPED = 'skipped'
    OFFLINE = 'offline'
    OFFLINE_TIMESTAMP = 'offline_timestamp'
    INCOGNITO = 'incognito_mode'


class REASON_START:
    TRACK_DONE = 'trackdone'
    FORWARD_BUTTON = 'fwdbtn'
    APP_LOAD = 'appload'
    PLAY_BUTTON = 'playbtn'
    CLICK_ROW = 'clickrow'
    BACK_BUTTON = 'backbtn'
    TRACK_ERROR = 'trackerror'
    UNKNOWN = 'unknown'
    REMOTE = 'remote'


class REASON_END:
    TRACK_DONE = 'trackdone'
    FORWARD_BUTTON = 'fwdbtn'
    UNEXPECTED_EXIT_WHILE_PAUSED = 'unexpected-exit-while-paused'
    LOGOUT = 'logout'
    ENDPLAY = 'endplay'
    BACK_BUTTON = 'backbtn'
    REMOTE = 'remote'
    UNEXPECTED_EXIT = 'unexpected-exit'
    UNKNOWN = 'unknown'


class PLATFORM:
    ANDROID = 'android'
    LINUX = 'linux'
    WINDOWS = 'windows'


class VIDEO_FIELD:
    TIMESTAMP = 'ts'


