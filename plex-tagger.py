import os
from plexapi.server import PlexServer

PLEX_URL = os.getenv("PLEX_URL")
PLEX_TOKEN = os.getenv("PLEX_TOKEN")

plex = PlexServer(PLEX_URL, PLEX_TOKEN)
results = plex.library.search(resolution="4k",libtype="movie")
for movie in results:
  movie.addLabel("4K")
  print(f"Adding tag \"4K\" to movie {movie.title}")