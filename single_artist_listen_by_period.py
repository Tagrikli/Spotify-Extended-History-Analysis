import pandas as pd
import plotly.express as px
import plotly.io as pio
from consts import AUDIO_FIELD
from paths import PATH_FILE_AUDIO_PKL
from utils import apply_filters


ARTIST_NAME = 'Fiona Apple'
SKIPPED = False
PERIOD = '1M'


df = pd.read_pickle(PATH_FILE_AUDIO_PKL)
df = apply_filters(df, skipped=False)
df = df[df[AUDIO_FIELD.SKIPPED] == SKIPPED]
df = df[df[AUDIO_FIELD.ARTIST_NAME] == ARTIST_NAME]


df['period'] = df[AUDIO_FIELD.TIMESTAMP].dt.to_period(PERIOD).astype(str)

grouped_period = df.groupby(['period']).agg(
    count=(AUDIO_FIELD.TRACK_NAME, 'size'),
    tracks=(AUDIO_FIELD.TRACK_NAME, lambda x: '<br>'.join(x.unique()))
).reset_index()

# grouped_period = df.groupby(['period']).size().reset_index(name='count')

print(grouped_period)
# exit()

fig = px.bar(grouped_period,
             x='period',
             y='count',
             title=f"Track counts per {PERIOD}",
             labels={'period': 'Time Period', 'count': 'Track Count'},
             hover_data=['tracks'])

hovertemplate = '<b>Period:</b> %{x}<br><b>Artist Name:</b> ' + ARTIST_NAME + \
    '<br><b>Track Count:</b> %{y}<br><b>Track Names:</b> %{customdata}'


fig.update_traces(hovertemplate=hovertemplate)
fig.show()
