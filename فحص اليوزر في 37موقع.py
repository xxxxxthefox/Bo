import random 
import os,urllib
try:
	import telebot
except ModuleNotFoundError:
	os.system('pip install pyTelegramBotApi')	
	
'''DEV»  @b_4qr
CH» @baqertools'''
	
from telebot import *
bot = telebot.TeleBot('7498013463:AAHylRVx4nqhh5gF4JTfH-7JHlpai43ecf8')
@bot.message_handler(commands=["start"])
def start(message):
	bot.send_message(message.chat.id,'-اهلا في بوت فحص اليوزر المتاح في سوشل ميديا •')      
         
@bot.message_handler(func=lambda message:True)
def send_message(message):
    bot.send_message(message.chat.id,'انتضر رجا...⏳')
    user=message.text
    domen =['https://www.tradingview.com/u/','https://www.twitch.tv/','https://www.youtube.com/','https://www.reddit.com/user/','https://www.snapchat.com/add/','https://www.zhihu.com/people/','https://t.me/','https://www.roblox.com/user.aspx?username=','https://trello.com/','https://genius.com/','https://www.duolingo.com/profile/','https://tr.op.gg/summoner/userName=','https://lan.op.gg/summoner/userName=','https://euw.op.gg/summoner/userName=','https://na.op.gg/summoner/userName=','https://ru.op.gg/summoner/userName=','https://www.wattpad.com/user/','https://lichess.org/@/','https://adultfriendfinder.com/profile/','https://osu.ppy.sh/users/','https://forum.fanat1k.ru/member.php?username=','https://forum.truckersmp.com/index.php?/search/&q=&type=core_members','https://www.trainsim.com/vbts/member.php?username=','http://forum.vegalab.ru/member.php?username=','https://www.autolada.ru/profile.php?mode=viewprofile&u=','https://www.paypal.com/paypalme/','http://www.motorhomefun.co.uk/forum/members/?username=','https://forum-b.ru/search.php?action=search&keywords=&author=','https://www.bandlab.com/api/v1.3/users/','https://api.fotka.com/v2/user/dataStatic?login=','https://www.friendfinder-x.com/profile/','https://exploretalent.com/','https://irl.com/','https://www.threads.net/@','https://www.instagram.com/@']
    for baqer in domen :
    	baqer1 = baqer+user
    	try :
    	   openurl = urllib.request.urlopen(baqer1)
    	   bot.send_message(message.chat.id,'غير متاح ❌'+'»»'+baqer1)      
    	except urllib.error.URLError as msg :
    		bot.send_message(message.chat.id,'متاح ✅'+'»»'+baqer1)  
    		
    		        
'''DEV»  @b_4qr
CH» @baqertools'''
		   	
bot.infinity_polling()
