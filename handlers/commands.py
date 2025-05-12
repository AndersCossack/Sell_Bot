from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

router = Router()

template = """<i>м. Київ, вул. Мішуги, ТЦ "Піраміда"</i> 
Продав: <b>{text}</b>"""

@router.message()
async def handler_messages(message: Message):
    if message.text:
        formatted_text = template.format(text=message.text)
        await message.answer(formatted_text, parse_mode="HTML")
