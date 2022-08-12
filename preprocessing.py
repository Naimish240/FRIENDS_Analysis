import re
import glob
import pandas as pd


def process_scripts(path):
    df = []

    def read_script(pth):
        S_E = pth.split()[0][13:]
        season = int(S_E[1:3])
        episode = int(S_E[4:6])
        title = pth.split(" ", maxsplit=1)[1][:-4]

        foo = []

        with open(pth, 'r') as fh:
            lines = fh.readlines()

        for line in lines:
            temp = re.sub("[\(\[].*?[\)\]]", "", line)
            # Ignore lines that start with '[', because they set up locaiton
            if not temp:
                continue

            if temp[0] == '[' or temp[0] == '(' or temp[0] == '\n' or temp[0] == '{':
                continue
            # Ignore lines without a ':', because no speaker
            if ':' not in temp:
                continue
            speaker, dialog = temp.split(':', maxsplit=1)
            dialog = dialog.strip('\n')
            foo.append([season, episode, title, speaker, dialog])

        return foo
    
    scripts = glob.glob("data/scripts/*.txt")
    
    for script in scripts:
        print(script)
        data = read_script(script)
        for foo in data:
            df.append(foo)

    print(len(df), len(df[0]))
    df = pd.DataFrame(df, columns=["Season", "Episode", "Title", "Speaker", "Dialog"])
    print(df.head())
    print(df.Speaker.unique())
    # return df


def process_ratings(path):
    pass


def process_viewership(path):
    pass


def save_dialogues(df):
    pass


def save_metadata(df):
    pass


def main():
    print(process_scripts("data/scripts"))


if __name__ == '__main__':
    main()
