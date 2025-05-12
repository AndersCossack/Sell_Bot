from aiogram import F, Router
from aiogram.types import Message, CallbackQuery

call_router = Router()

import keyboards.inline_kb as ikb

@call_router.message(F.text == "Меню")
async def menu(message: Message):
    await message.answer("Виберіть пункт меню: ", reply_markup=ikb.inline_kb)