from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from dotenv import load_dotenv
import os

load_dotenv()

token = os.environ.get("TOKEN")
bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Приветствую, я Бот SS-14.865.7654.NT(7658932), моя основная задача продовать оружее, вот список команд:/HELP-узнать дригие функции бота')
    await message.answer('Приятного дня')

@dp.message_handler(commands='HELP')
async def help(message: types.Message):
    await message.answer('просмотр оружея: Гладкоствольное оружие 12 калибра(/G), Снайперская винтовка Драгунова(/D), Ручной пулемёт Дегтярёва(/PGD), FN FAL(/F), АК-47(/AK)')

@dp.message_handler(commands='AK')
async def AK(message: types.Message):
    await message.answer('Калибр    7,62 мм, Применяемый патрон    7,62х39 мм, Длина    870 мм, Длина ствола    415 мм, Масса (без патронов)    4,3 кг, Масса (с патронами)    4,876 кг, Прицельна дальность стрельбы    800 м, Темп стрельбы    600 в/м, Скорострельность очередями    400 в/м,  Скорострельность одиночным огнем    90-100 в/м, Начальная скорость полета пули    715 м/с, Емкость магазина    30 патронов, узнать больше:https://ru.wikipedia.org/wiki/%D0%90%D0%B2%D1%82%D0%BE%D0%BC%D0%B0%D1%82_%D0%9A%D0%B0%D0%BB%D0%B0%D1%88%D0%BD%D0%B8%D0%BA%D0%BE%D0%B2%D0%B0, купить:https://paritetsv.ru/oruzhie/raritet/ma-136')

@dp.message_handler(commands='D')
async def g(message: types.Message):
    await message.answer('https://ru.wikipedia.org/wiki/%D0%A1%D0%BD%D0%B0%D0%B9%D0%BF%D0%B5%D1%80%D1%81%D0%BA%D0%B0%D1%8F_%D0%B2%D0%B8%D0%BD%D1%82%D0%BE%D0%B2%D0%BA%D0%B0_%D0%94%D1%80%D0%B0%D0%B3%D1%83%D0%BD%D0%BE%D0%B2%D0%B0, купить:https://www.air-gun.ru/karabiny-svd')

@dp.message_handler(commands='G')
async def y(message: types.Message):
    await message.answer('Huglu Hawk Silver 12x76 L=760 характеристики:Емкость магазина	2, Вес (кг)	2,7, Материал корпуса	металл/дерево, Тип ствола	гладкий, Производитель	Huglu (Турция), Общая длина	1150 мм, Патронник, мм	76, Материал ствола	оружейная сталь 4140, Длина ствола, см	76, Предохранитель	есть, Калибр	12, Материал цевья	дерево, Материал приклада	дерево, Экстрактор	да, Спусковые крючки	1, Способ снаряжения	переломное, Кол-во стволов	два ствола (вертикалка), Режим стрельбы	одиночный, Вид	ружье, купить:https://www.air-gun.ru/gladkostvolnoe_oruzhie/huglu/ruje-huglu-hawk-silver-12h76-l760-mm')

@dp.message_handler(commands='PGD')
async def rgd(message: types.Message):
    await message.answer("Ручной пулемёт Дегтярёва, характеристики: Разработан: 1944 год, Вид боепитания: лента на 100 патронов в круглом металлическом коробе, Годы эксплуатации: 1945-2000 годы, Длина ствола, мм: 520, Калибр, мм: 7,62, Максимальная дальность, м: 800 (эффективная), Масса, кг: 7,4 (с коробкой и неснаряжённой лентой); 9 (с коробкой и снаряжённой лентой); 0,8 (коробка с лентой без патронов), узнать больше:https://ru.wikipedia.org/wiki/%D0%A0%D1%83%D1%87%D0%BD%D0%BE%D0%B9_%D0%BF%D1%83%D0%BB%D0%B5%D0%BC%D1%91%D1%82_%D0%94%D0%B5%D0%B3%D1%82%D1%8F%D1%80%D1%91%D0%B2%D0%B0, купить:https://popadiv10.ru/ruchnoy-pulemet-rpd-44-sh-degtyareva-oholoshchenny/")

@dp.message_handler(commands='F')
async def f(message: types.Message):
    await message.answer('FN FAL, характеристики: Конструктор: Дьёдонне Сэв; Эрнест Вервье, Разработан: 1951 год, Вид боепитания: отъёмный коробчатый магазин на 20 или 30 (вариант ручного пулемёта) Также доступны барабанные магазины на 50 патронов, Годы производства: 1953 год — настоящее время, Длина ствола, мм: 533; 431 (50.63), Калибр, мм: 7,62, Максимальная дальность, м: 500 (эффективная), узнать больше:https://ru.wikipedia.org/wiki/FN_FAL, купить:https://cccp-gun.ru/shop/4228/desc/okholoshhennaja-shturmovaja-vintovka-fn-fal-skhp-rossija-rok ')

if __name__ == '__main__':
    executor.start_polling(dp)