import pandas as pd
import json
import os
import sys
import pickle as pkl
import plotly.express as px

import plotly.io as pio

from consts import AUDIO_FIELD, REASON_START
from paths import PATH_FILE_AUDIO_PKL
from utils import apply_filters


PERIOD = '1M'

df = pd.read_pickle(PATH_FILE_AUDIO_PKL)
df = apply_filters(df, skipped=False, reason_start=None)


df['period'] = df[AUDIO_FIELD.TIMESTAMP].dt.to_period(PERIOD)


grouped_period = df.groupby(
    ['period', AUDIO_FIELD.TRACK_NAME]).size().reset_index(name='count')


most_listened = grouped_period.loc[grouped_period.groupby('period')[
    'count'].idxmax()]
most_listened['period'] = most_listened['period'].dt.start_time
most_listened = most_listened.sort_values(AUDIO_FIELD.TRACK_NAME)


fig = px.bar(most_listened,
             x='period',
             y='count',
             color=AUDIO_FIELD.TRACK_NAME,
             title=f"Top Tracks of {PERIOD}",
             labels={'period': 'Time Period', 'count': 'Listen Count',
                     AUDIO_FIELD.TRACK_NAME: 'Track Name'},
             text=AUDIO_FIELD.TRACK_NAME)



fig.show()
