import pandas as pd

from download import download_files_list, download_file
from upload import upload_file

def main():
    f = open("files_list.data", "r")
    used_files = str.splitlines(f.read())
    new_files = download_files_list()

    for filename in new_files:
        if not filename in used_files:
            df = pd.DataFrame.from_dict(download_file(filename))

            songs = convert(df, 'song')
            movies = convert(df, 'movie')
            apps = convert(df, 'app')

            upload(songs, 'songs')
            upload(movies, 'movies')
            upload(apps, 'apps')

def convert(df, data_type):
    df = df.loc[df['type'] == data_type]
    df1 = pd.DataFrame(df['data'].values.tolist())

    print(df1)

if __name__ == "__main__":
    main()