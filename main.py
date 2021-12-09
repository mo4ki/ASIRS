from telebot import *
from SimpleQIWI import *
from time import sleep
import os, Configs

print("Qiwi Токен (" + Configs.QiwiToken + ") активен до 06.04.2022, после этого нужно будетвыпустить новый")

bot = telebot.TeleBot(Configs.TGToken, parse_mode="HTML")

# Команда старт
@bot.message_handler(commands=['start'])
def text(message):
	bot.send_message(message.chat.id, "<b>Привет!</b>")

	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	itembtn1 = types.KeyboardButton('Купить подписку')
	itembtn2 = types.KeyboardButton('Подробнее')
	markup.add(itembtn1, itembtn2)

	sleep(0.5)
	bot.send_message(message.chat.id, Configs.HelloMessage, reply_markup=markup)

# Текст
@bot.message_handler(content_types=['text'])
def text(message):

	if message.text.lower() == "подробнее":
		bot.send_message(message.chat.id, Configs.podrobnee)

	elif message.text.lower() == "купить подписку":
		api = QApi(token=Configs.QiwiToken, phone=Configs.phone)

		api.start()

		price = 10
		comment = api.bill(price)   # Создаем счет. Комментарий с которым должен быть платеж генерируется автоматически, но его можно задать                                 # параметром comment. Валютой по умолчанию считаются рубли, но ее можно изменить параметром currency
		
		oplata =  """
<b>Оплата МЕСЯЧНОЙ подписки на SsStealer</b>

Для получения подписки Вам необходимо перевести на Qiwi кошелек денежную сумму в размере """ + str(price) + """ рублей, указав комментарий (обязательно, не указав его автоматическая проверка не сможет проверить Ваш платеж)

<b>Кошелек Qiwi:</b> """ + Configs.phone + """
<b>Комментарий:</b> """ + comment + """
<b>Сумма перевода:</b> """ + str(price) + """ рублей

<b>Внимание!</b> После оплаты нажмите на соотвествующую кнопку для проверки Вашего платежа!
		"""

		markup = types.InlineKeyboardMarkup(row_width=1)
		item = types.InlineKeyboardButton('Проверить оплату', callback_data='question_1')
		markup.add(item)

		bot.send_message(message.chat.id, oplata, reply_markup=markup)

		@bot.callback_query_handler(func=lambda call:True)
		def callback(call):
			if call.message:
				if call.data == 'question_1':
					if api.check(comment):  # Проверяем статус
						api.stop()  # Останавливаем прием платежей

						bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= Configs.oplata)
						bot.answer_callback_query(call.id, text="Платёж получен!")

						print("Оплата получена!") # Здесь есть место для логирования людей что купили мой стиллер 
						if os.path.exists("Users.txt") == False:
							FUsers = open("Users.txt", "a")
							FUsers.write("")

						TFUsers = open("Users.txt")
						text = TFUsers.read()
						TFUsers.close

						if str(call.from_user.username) in str(text):
							pass

						else:
							FUsers = open("Users.txt", "a")
							FUsers.write("User: " + str(call.from_user.username) + "; UserID: " + str(call.from_user.id)+ "\n")
						FUsers.close()

						builder(True, call.from_user.id)

					else:
						bot.answer_callback_query(call.id, text="Оплата не получена!")

def builder(Kitty, Userid):
	pass

bot.polling()