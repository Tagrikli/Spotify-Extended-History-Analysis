import pandas as pd
import plotly.express as px
from consts import AUDIO_FIELD
from paths import PATH_FILE_AUDIO_PKL
from utils import apply_filters


df = pd.read_pickle(PATH_FILE_AUDIO_PKL)

track_count = df[AUDIO_FIELD.ARTIST_NAME].value_counts(
    sort=True, ascending=False).reset_index()

fig = px.bar(x=track_count[AUDIO_FIELD.ARTIST_NAME], y=track_count['count'])
fig.update_xaxes(tickangle=45)

fig.show()
