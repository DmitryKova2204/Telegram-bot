from aiogram.types import Message
from datetime import timedelta
import schedule
def cabinet(message: Message):
    print(message.date + timedelta(hours=2))
    weekDay = message.date.weekday()
    orario = schedule.Schedule
    print(orario.get_lesson_time(orario))

