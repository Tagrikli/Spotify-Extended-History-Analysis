import pandas as pd
import plotly.express as px
import plotly.io as pio
from consts import AUDIO_FIELD
from paths import PATH_FILE_AUDIO_PKL
from utils import apply_filters


df = pd.read_pickle(PATH_FILE_AUDIO_PKL)
df = apply_filters(df, skipped=False)

unique_songs_per_artist = df.groupby(AUDIO_FIELD.ARTIST_NAME)[AUDIO_FIELD.TRACK_NAME].nunique().reset_index()
unique_songs_per_artist.columns = ['Artist Name', 'Unique Song Count']

unique_songs_per_artist = unique_songs_per_artist.sort_values('Unique Song Count', ascending=False)
# Create a bar chart
fig = px.bar(unique_songs_per_artist, 
             x='Artist Name', 
             y='Unique Song Count', 
             title="Number of Unique Tracks Listened Per Artist",
             labels={'Artist Name': 'Artist', 'Unique Song Count': 'Unique Song Count'})

fig.update_layout(xaxis=dict(title="Artist Name"), yaxis=dict(title="Unique Song Count"))
fig.show()
