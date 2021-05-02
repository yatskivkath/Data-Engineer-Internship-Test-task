import pandas as pd
import datetime as dt
import re

from download import download_files_list, download_file
from upload import upload_file

def main():
    read = open("files_list.data", "r")
    used_files = str.splitlines(read.read())
    new_files = download_files_list()

    write = open("files_list.data", "a")
    for filename in new_files:
        if not filename in used_files:
            send(pd.DataFrame.from_dict(download_file(filename)))
            write.write(filename +'\n')

            print(filename, " LOADED")
    
    write.close()

            

def send(df):
    songs = convert(df, 'song')
    movies = convert(df, 'movie')
    apps = convert(df, 'app')

    songs['ingestion_time'] = pd.to_datetime(dt.datetime.now())
    movies['original_title_normalized'] = movies['original_title'].apply(lambda x: re.sub('[^0-9a-zA-Z_]+', '', x.casefold().replace(' ', '_') ))
    apps['is_awesome'] = apps['rating'] >= 4.5 

    upload_file(songs, 'songs')
    upload_file(movies, 'movies')
    upload_file(apps, 'apps')

def convert(df, data_type):
    df = df.loc[df['type'] == data_type]
    df1 = pd.DataFrame(df['data'].values.tolist())

    return df1

if __name__ == "__main__":
    main()