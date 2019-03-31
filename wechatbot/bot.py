from wxpy import *
from parsecsv import parse_csv

global bot
global tuling
global key_value_set
tuling = Tuling(api_key='da70c68524fc4d21be4ba474c955d70e')
bot = Bot()

#print(bot.groups()) #群聊
#print(bot.mps()) #公众号
key_value_set = parse_csv('test.csv')

tempgroup = bot.groups().search('temp')
print(tempgroup)

#@bot.register(tempgroup)
@bot.register(bot.friends())
def reply_my_friend(msg):
	print(msg)
	print(msg.text)
	if msg.text in key_value_set.keys():
		print('return value')

		try:
			print(key_value_set[msg.text])
			msg.reply(key_value_set[msg.text])
		except Exception as e:
			print("sth wrong with send_msg")
	else:	
		print("tuling reply:")
		tuling.do_reply(msg)



@bot.register(tempgroup)
def auto_reply(msg):
	print(msg)
	print(msg.__repr__)
	print(msg.text)
	print(msg.type)
	print("at or not at")
	print(msg.is_at)
	print(isinstance(msg.chat, Group))
	if isinstance(msg.chat, Group) and msg.is_at: 
		print("inside")
		realtext = msg.text.replace('@'+bot.self.name, '').strip()
		print(realtext)
		if realtext in key_value_set.keys():

			try:
				print(key_value_set[realtext])
				msg.reply(key_value_set[realtext])
			except Exception as e:
				print("sth wrong with send_msg")
		else:	
			print("tuling reply:")
			try:

				tuling.do_reply(msg)
			except Exception as e:
				print("group tuling reply failed")
	else:
		print("else")


embed()


