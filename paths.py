import os


CWD = os.getcwd()

PATH_FILE_ZIP = os.path.join(CWD, 'my_spotify_data.zip')
PATH_FILE_UNZIP = os.path.join('my_spotify_data')

PATH_FOLDER_RAW_DATA = os.path.join(
    CWD, 'my_spotify_data', 'Spotify Extended Streaming History')
PATH_FOLDER_DATA = os.path.join(CWD, 'data')

PATH_FILE_AUDIO_PKL = os.path.join(PATH_FOLDER_DATA, 'all_spotify_audio.pkl')
PATH_FILE_VIDEO_PKL = os.path.join(PATH_FOLDER_DATA, 'all_spotify_video.pkl')
PATH_FILE_AUDIO_JSON = os.path.join(PATH_FOLDER_DATA, 'all_spotify_audio.json')
PATH_FILE_VIDEO_JSON = os.path.join(PATH_FOLDER_DATA, 'all_spotify_video.json')
