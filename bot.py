import asyncio
import os
import subprocess
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command  # Оновлений імпорт для фільтрів
from aiogram.types import Message

# Вкажіть свій токен
TOKEN = "https://myrouterxiaomi.ddns.net"
# IP-адреса або домен роутера
ROUTER_IP = "192.168.31.1"

bot = Bot(token=TOKEN)
dp = Dispatcher()

def ping_router(ip: str) -> bool:
    """Перевіряє доступність роутера через ping."""
    param = "-n" if os.name == "nt" else "-c"
    command = ["ping", param, "1", ip]
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.returncode == 0
    except Exception:
        return False

@dp.message(Command("start"))  # Оновлений спосіб реєстрації команд
async def start(message: Message):
    await message.answer("Привіт! Введи команду /check для перевірки доступності роутера.")

@dp.message(Command("check"))  # Оновлений спосіб реєстрації команд
async def check_router(message: Message):
    await message.answer("Перевіряю доступність роутера...")
    available = ping_router(ROUTER_IP)
    if available:
        await message.answer("✅ Роутер доступний!")
    else:
        await message.answer("❌ Роутер не відповідає! Перевір з'єднання.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
