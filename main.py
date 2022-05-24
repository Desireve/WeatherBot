import config
import logging
from aiogram import Bot, Dispatcher, executor, types
import pogod_module
import translate
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
    name_gorod = msg.text
    name_gorod = translate.RuToEng(name_gorod)
    try:
        temp = pogod_module.get_temp(name_gorod)
        osadki = pogod_module.get_osadki_status(name_gorod)
        windspeed = pogod_module.get_wind_speed(name_gorod)
        otvet = "Погода в "+msg.text +"\n"
        otvet += "Сейчас: \n"
        otvet += "Температура: " + str(temp.get('temp', 'нет данных')) + "\n"
        otvet += "Максимум: " + str(temp.get('temp_max', 'нет данных')) + "\n"
        otvet += "Минимум: " + str(temp.get('temp_min', 'нет данных')) + "\n"
        otvet += "Ощущается как: " + str(temp.get('feels_like', 'нет данных')) + "\n"
        otvet += "Осадки:" + str(translate.EngToRu(osadki)) + "\n"
        otvet += "Скорость ветра: " + str(windspeed) +" m/s \n"
        await bot.send_message(msg.from_user.id, otvet)
    except:
        errortext = "Возникла какая то ошибка, либо я не знаю такого города"
        await bot.send_message(msg.from_user.id, errortext)
    


# запускаем лонг поллинг
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)