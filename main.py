import config
import logging
from aiogram import Bot, Dispatcher, executor, types
import pogod_module

# Задаем уровень логов
logging.basicConfig(level=logging.INFO)

# Инициализация бота
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)





# команда
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Привет!\nНапиши название города на английском языке, а я пришлю погодную информацию")

@dp.message_handler()
async def pogoda_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, "Погода в "+msg.text)
    name_gorod = msg.text

    temp = pogod_module.get_pogoda(name_gorod)

    otvet = "Температура: " + str(temp.get('temp', 'нет данных')) + "\n"
    otvet += "Максимум: " + str(temp.get('temp_max', 'нет данных')) + "\n"
    otvet += "Минимум: " + str(temp.get('temp_min', 'нет данных')) + "\n"
    otvet += "Ощущается как: " + str(temp.get('feels_like', 'нет данных')) + "\n"
    
    await bot.send_message(msg.from_user.id, otvet)
    


# запускаем лонг поллинг
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)