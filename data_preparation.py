import os
import zipfile
import pandas as pd
from paths import PATH_FILE_AUDIO_JSON, PATH_FILE_AUDIO_PKL, PATH_FILE_UNZIP, PATH_FILE_VIDEO_JSON, PATH_FILE_VIDEO_PKL, PATH_FILE_ZIP, PATH_FOLDER_RAW_DATA, PATH_FOLDER_DATA
from consts import AUDIO_FIELD, VIDEO_FIELD
from loguru import logger

logger.info('Unzipping...')
# Unzipping
with zipfile.ZipFile(PATH_FILE_ZIP, 'r') as zip_ref:
    zip_ref.extractall(PATH_FILE_UNZIP)


logger.info('Creating required folders.')
# Listing files
files_json = [f for f in os.listdir(
    PATH_FOLDER_RAW_DATA) if f.endswith('.json')]
files_json_audio = [f for f in files_json if 'Audio' in f]
files_json_video = [f for f in files_json if 'Video' in f]

os.makedirs(PATH_FOLDER_DATA, exist_ok=True)

logger.info('Combining audio files...')
### COMBINE AUDIO ###

# All audio JSONs to dataframes.
dfs_audio = []
for filename in files_json_audio:
    filepath = os.path.join(PATH_FOLDER_RAW_DATA, filename)
    df = pd.read_json(filepath)
    logger.info(f'{filename}: {df.size} records.')
    dfs_audio.append(df)

# Concat all dataframes
df_audio = pd.concat(dfs_audio, ignore_index=True)

# Field type conversion and sorting.
df_audio[AUDIO_FIELD.TIMESTAMP] = pd.to_datetime(df_audio[AUDIO_FIELD.TIMESTAMP])
df_audio = df_audio.sort_values(by=[AUDIO_FIELD.TIMESTAMP], ascending=False)

# Save.
logger.info(f'Total record amount: {df_audio.size}')
df_audio.to_pickle(PATH_FILE_AUDIO_PKL)
df_audio.to_json(PATH_FILE_AUDIO_JSON, orient='records', indent=4)
###


logger.info('Combining video files.')
### COMBINE VIDEO ###

# All video JSONs to dataframes.
dfs_video = []
for filename in files_json_video:
    filepath = os.path.join(PATH_FOLDER_RAW_DATA, filename)
    df = pd.read_json(filepath)
    logger.info(f'{filename}: {df.size} records.')
    dfs_video.append(df)

# Concat all dataframes
df_video = pd.concat(dfs_video, ignore_index=True)

# Field type conversion and sorting.
df_video[VIDEO_FIELD.TIMESTAMP] = pd.to_datetime(df_video[VIDEO_FIELD.TIMESTAMP])
df_video = df_video.sort_values(by=[VIDEO_FIELD.TIMESTAMP], ascending=False)

# Save.
logger.info(f'Total record amount: {df_video.size}')
df_video.to_pickle(PATH_FILE_VIDEO_PKL)
df_video.to_json(PATH_FILE_VIDEO_JSON, orient='records', indent=4)
###

logger.info('Bye.')