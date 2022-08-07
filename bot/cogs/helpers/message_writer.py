from xmlrpc.client import Boolean
import pandas as pd

def get_data(messages, what_to_find)->Boolean:
    data = pd.DataFrame(columns=['content', 'time', 'author', 'channel'])
    if not messages:
        return False
    for msg in messages:
        if msg.content.find(what_to_find) != -1:
            data = data.append({'content': msg.content, 'time': msg.created_at,
                                'author': msg.author, 'channel': msg.channel.name}, ignore_index=True)
    print(data)
    return True


if __name__ == '__main__':
    print('This file can only be run from Bot.py')
