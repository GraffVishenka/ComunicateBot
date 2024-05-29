import telebot;
from telebot import types
from consts import *;

bot = telebot.TeleBot(botAPI);

@bot.message_handler(commands=["start"])
def main(message):
  bot.send_message(message.from_user.id, "Ещё раз здравствуй, как я могу к тебе обращаться?");
  bot.register_next_step_handler(message, get_name)

@bot.message_handler(commands=["recomindations"])
def main(message):
  for i in range (0, len(recomindationText)):
      bot.send_photo(message.from_user.id, recomindationImg[i], caption=recomindationText[i])

@bot.message_handler(commands=["books"])
def main(message):
  for i in range (0, len(books)):
      bot.send_message(message.from_user.id, f"{books[i]}\n\n{booksUrl[i]}");

@bot.message_handler(commands=["places"])
def main(message):
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  btn1 = types.KeyboardButton("Музеи")
  btn2 = types.KeyboardButton("Активный отдых")
  btn3 = types.KeyboardButton("Пространства для коммуникации")
  btn4 = types.KeyboardButton("Театры")
  btn5 = types.KeyboardButton("Кофейни")
  btn6 = types.KeyboardButton("Назад")
  markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
  bot.send_message(message.from_user.id, placeText, reply_markup=markup);

@bot.message_handler(commands=["groups"])
def main(message):
  bot.send_message(message.from_user.id, f"Группы где можно узнать о различных мероприятиях в Тюмени:\n\n{vkGroup}");

@bot.message_handler(commands=["museum"])
def main(message):
  for i in range (0, len(museum)):
      bot.send_message(message.from_user.id, museum[i]);

@bot.message_handler(commands=["outdooractivity"])
def main(message):
  for i in range (0, len(outdoorActivity)):
      bot.send_message(message.from_user.id, outdoorActivity[i]);

@bot.message_handler(commands=["theatre"])
def main(message):
  for i in range (0, len(theatre)):
      bot.send_message(message.from_user.id, theatre[i]);

@bot.message_handler(commands=["space"])
def main(message):
  for i in range (0, len(spacesForCommunication)):
      bot.send_message(message.from_user.id, spacesForCommunication[i]);

@bot.message_handler(commands=["coffee"])
def main(message):
  for i in range (0, len(coffee)):
      bot.send_message(message.from_user.id, coffee[i]);

@bot.message_handler(commands=["help"])
def main(message):
      bot.send_message(message.from_user.id, get_name_2);

def get_name(message):
  global name
  name = message.text
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  btn1 = types.KeyboardButton("Рекомендации")
  btn2 = types.KeyboardButton("Книги")
  btn4 = types.KeyboardButton("Места Тюмени")
  btn3 = types.KeyboardButton("Группы ВК")
  markup.add(btn1, btn2, btn4 ,btn3)
  if name.lower() != "назад":
    bot.send_message(message.from_user.id, f"Приятно познакомится, {name}!");
  bot.send_message(message.from_user.id, get_name_2);
  bot.send_message(message.from_user.id, get_name_3, reply_markup=markup);

@bot.message_handler(content_types=['text'])
def main(message):
  if message.text.lower() == 'рекомендации':
    for i in range (0, len(recomindationText)):
      bot.send_photo(message.from_user.id, recomindationImg[i], caption=recomindationText[i])
  elif message.text.lower() == 'книги':
    for i in range (0, len(books)):
      bot.send_message(message.from_user.id, f"{books[i]}\n\n{booksUrl[i]}");
  elif message.text.lower() == 'места тюмени':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Музеи")
    btn2 = types.KeyboardButton("Активный отдых")
    btn3 = types.KeyboardButton("Пространства для коммуникации")
    btn4 = types.KeyboardButton("Театры")
    btn5 = types.KeyboardButton("Кофейни")
    btn6 = types.KeyboardButton("Назад")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    bot.send_message(message.from_user.id, placeText, reply_markup=markup);
  elif message.text.lower() == 'группы вк':
    bot.send_message(message.from_user.id, f"Группы где можно узнать о различных мероприятиях в Тюмени:\n\n{vkGroup}");
  elif message.text.lower() == 'назад':
    get_name(message)
  elif message.text.lower() == 'музеи':
    for i in range (0, len(museum)):
      bot.send_message(message.from_user.id, museum[i]);
  elif message.text.lower() == 'активный отдых':
    for i in range (0, len(outdoorActivity)):
      bot.send_message(message.from_user.id, outdoorActivity[i]);
  elif message.text.lower() == 'театры':
    for i in range (0, len(theatre)):
      bot.send_message(message.from_user.id, theatre[i]);
  elif message.text.lower() == 'пространства для коммуникации':
    for i in range (0, len(spacesForCommunication)):
      bot.send_message(message.from_user.id, spacesForCommunication[i]);
  elif message.text.lower() == 'кофейни':
    for i in range (0, len(coffee)):
      bot.send_message(message.from_user.id, coffee[i]);
  else:
    bot.send_message(message.from_user.id, errorText);

bot.polling(none_stop=True);