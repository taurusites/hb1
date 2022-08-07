import pandas as pd

def write_file(data):
    try:
        file_location="data.csv"
        data.to_csv(file_location)
    except:
        return False
    return True


def get_data(messages, what_to_find):
    data = pd.DataFrame(columns=['content', 'time', 'author', 'channel'])
    retval = False
    if messages:
        for msg in messages:
            if msg.content.find(what_to_find) != -1:
                data = data.append({'content': msg.content, 'time': msg.created_at,
                                'author': msg.author, 'channel': msg.channel.name}, ignore_index=True)
        if write_file(data):
            retval = True
        else:
            retval = False
    return retval


if __name__ == '__main__':
    print('This file can only be run from Bot.py')
