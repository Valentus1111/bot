from aiogram import Router, types, F  # Импорт основных классов из aiogram
from aiogram.filters.command import Command  # Импорт фильтра команд из aiogram
import logging  # Импорт модуля логирования
import random  # Импорт модуля random для генерации случайных чисел
from keyboards.keyboards import keyboard
from utils.random_fox import fox

router = Router()

@router.message(Command(commands=['start']))  # Декоратор для обработки команды /start
async def start(message: types.Message):  # Асинхронная функция для реакции на команду /start
    await message.answer(f'Привет, {message.from_user.full_name}!', reply_markup=keyboard)  # Отправляем приветственное сообщение

@router.message(Command(commands=['stop']))
async def start(message: types.Message):
    await message.answer(f'Всего хорошего!')

@router.message(Command(commands=['инфо', 'info']))
@router.message(F.text.lower() == 'инфо')
async def start(message: types.Message):
    number = random.randint(1, 100)
    await message.answer(f'Привет, твое число: {number}!')


@router.message(F.text.lower() == 'покажи лису')
async def info(message: types.Message):
    img_fox = fox()
    await message.answer('Лови лису')
    await message.answer_photo(img_fox)