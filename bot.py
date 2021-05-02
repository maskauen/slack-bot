import slack

import config

token = config.SLACK_TOKEN
client = slack.WebClient(token=token)

client.chat_postMessage(channel='#test', text='show de la show')
