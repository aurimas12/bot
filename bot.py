import os
from dotenv import load_dotenv
import asyncio
from aiogram import Bot,Dispatcher,F
from aiogram.filters import Command,CommandObject
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.types import Message
import random

load_dotenv()

API_KEY=os.getenv('API_KEY')
bot=Bot(API_KEY)

dp=Dispatcher()


@dp.message(Command("start"))
async def start(message:Message):
    await message.answer(f"Hello,{message.from_user.first_name}")


@dp.message(Command(commands=["rn",'number']))
async def get_random_number(message:Message,command=CommandObject):
    a,b=[int(n) for n in command.args.split("-")]
    rnum=random.randint(a,b)

    await message.reply(f"Random number: {rnum}")


@dp.message(F.text=="play")
async def play_games(message:Message):
    x=await message.answer_dice(DiceEmoji.BASKETBALL)
    print(x.dice.value)

    
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())