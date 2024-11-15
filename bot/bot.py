import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import StateFilter
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from parser import parser
import TOKEN

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=TOKEN.TOKEN)
# Диспетчер
dp = Dispatcher()

class WaitDescription(StatesGroup):
    waiting_for_description = State()
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer('Hello')

@dp.message(Command("PoweCreate"),StateFilter(None))
async def cmd_power(message: types.Message, state : FSMContext):
    await state.set_state(WaitDescription.waiting_for_description)
    await message.answer('Пришли тему по которой ты хочешь создать презентацию')


@dp.message(F.text,StateFilter(WaitDescription.waiting_for_description))
async def get_description(message: types.Message, state: FSMContext):
    PROMT = message.text
    await message.answer('Я Я Я, я гей')
    await state.clear()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":

    asyncio.run(main())