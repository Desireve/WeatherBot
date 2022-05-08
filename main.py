import config
import logging
from aiogram import Bot, Dispatcher, executor, types

# Задаем уровень логов
logging.basicConfig(level=logging.INFO)

# Инициализация бота
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)





# команда
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Привет!\nНапиши название города, а я пришлю и")

@dp.message_handler()
async def pogoda_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)
    name_gorod = msg.text


# запускаем лонг поллинг
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)