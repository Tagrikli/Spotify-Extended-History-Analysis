
import pandas as pd
from consts import AUDIO_FIELD
from paths import PATH_FILE_AUDIO_PKL


df = pd.read_pickle(PATH_FILE_AUDIO_PKL)

values = df[AUDIO_FIELD.REASON_START].unique()
print('Start Reasons:', values)

values = df[AUDIO_FIELD.REASON_END].unique()
print('End Reasons:', values)

values = df[AUDIO_FIELD.PLATFORM].unique()
print('Platforms:', values)
