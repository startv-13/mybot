from aiogram import Bot, Dispatcher, types, executor
from os import getenv
bot_token = getenv('BOT_TOKEN')
if not bot_token:
    exit('Ошибка, не найден токен')
bot = Bot(token=bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def cmd_start(msg: types.Message):
    await msg.answer('Привет, человек!')

@dp.message_handler(commands=['about'])
async def cmd_about(msg: types.Message):
    await msg.answer("""/start - Начало работы
    /about - Чем могу быть полезен
    /send - Пришлю эмоджи животного при команде /send [животное]
    /dice - Игра""")

@dp.message_handler(commands=['send'])
async def cmd_send(msg: types.Message):
    animals_emojis = {"cat": "😽", "dog": "🐶", "unicorn": "🦄"}
    args = msg.get_args()
    await msg.answer(animals_emojis.get(args, f'На выбор: {", ".join(animals_emojis.keys())}'))

@dp.message_handler(commands=['dice'])
async def cmd_dice(msg: types.Message):
    await msg.answer_dice(emoji='🎲')

if __name__=='__main__':
    executor.start_polling(dp)
