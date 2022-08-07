import pandas as pd

def get_data(messages, what_to_find):
    data = pd.DataFrame(columns=['content', 'time', 'author', 'channel'])
    if not messages:
        return False
    for msg in messages:
        if msg.content.find(what_to_find) != -1:
            data = data.append({'content': msg.content, 'time': msg.created_at,
                                'author': msg.author, 'channel': msg.channel.name}, ignore_index=True)
    try:
        file_location="data.csv"
        data.to_csv(file_location)
    except ValueError:
        return False
    return True


if __name__ == '__main__':
    print('This file can only be run from Bot.py')
