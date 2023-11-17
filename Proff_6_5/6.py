# Найти самого активного отправителя сообщений.
from collections import defaultdict


def best_sender(messages: list, senders: list) -> str:
    message_count = defaultdict(int)

    for sender, message in zip(senders, messages):
        message_count[sender] += len(message.split())

    return max(reversed(message_count.keys()), key=lambda x: message_count[x])

messages = ['Hi, Linda', 'Hi, Sam', 'How are you doing?']
senders = ['Sam Fisher', 'Linda', 'Sam Fisher']

print(best_sender(messages, senders))