from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message
import app.keyboards as kb
import schedule
import cabinet

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Ciao',reply_markup=kb.main)

@router.message(F.text == 'Orario')
async def orario(message: Message):
    orario = schedule.Schedule()
    await message.answer(text=orario.get_schedule_string(), reply_markup=kb.main)

@router.message(F.text == 'Aula')
async def aula(message: Message):
    cabinet.cabinet(message)
