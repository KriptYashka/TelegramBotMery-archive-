import random
import view.weather as weather
import view.anecdot as anektod


def hello(name=None):
    if name is not None:
        name = ", " + name
    text = [f"Приветик{name}! Очень рада, что у тебя появилось свободное время поговорить со мной😊",
            f"Мя-я-я-у! И тебе привет!",
            f"О{name}, как раз вспоминала о тебе, приветик☺️"]
    return random.choice(text)


def unknown_command():
    text = ["Я знаю только 2 языка: человечий и кошачий. ",
            "Мяу? Это ещё что такое?",
            "Хм... Даже не знаю, как на это ответить🤔",
            "Может ты случайно уснул на клавиатуре? Я не совсем поняла тебя."]
    return random.choice(text)


def how_are_you():
    text = ["Все хорошо, спасибо) Надеюсь, что у тебя тоже😊",
            "Всю ночь тыгыдыкала, теперь отдыхаю.",
            "Прекрасно! Сегодня же всемирный день кошек, не знал?\nДа ладно, это я тебя разыгрываю😄"]
    temp_today = weather.get_weather_average()
    if temp_today < -10:
        text.append("Сегодня пролежала дома, вообще на улицу в такой дубак не хочется гулять, бррр...🥶")
        text.append("Я залипла на снег, не мешай.")
        text.append(f"Вышла на балкон и поняла, что при {temp_today:.1f} больше на балкон не хочется выходить. "
                    "Даже молоко в миске замерзло!")
    elif temp_today < 0:
        text.append("Сделала себе горячее молоко с ")
        text.append("В такую погоду стараюсь спать около батарей.")
        text.append(f"Прохладно сегодня было. На улице {temp_today:.1f}, поэтому рыбку из пруда достать не удалось(")
    elif temp_today < 10:
        text.append(f"Смотрела на лужи, в отражении видела что-то милое, прекрасное и очень зеленое💚")
    elif temp_today < 20:
        text.append(f"Прошлась по своей улице, в пруду нашла свою любимую рыбку, когда-нибудь я обязательно"
                    f" познакомлюсь с ней поближе🐠")
    elif temp_today >= 20:
        text.append(f"Я счаслива, сейчас моя самая любимая температура - {temp_today:.1f}")
    return random.choice(text)


def yesterday_weather():
    text = list()
    temp_yesterday = weather.get_weather_average(1)
    if temp_yesterday < -10:
        text.append("Сегодня пролежала дома, вообще на улицу в такой дубак не хочется гулять, бррр...🥶")
        text.append("❄️Кругом один снег, юху!")
        text.append(f"Посмотрела в прогноз погоды и поняла, что при {temp_yesterday:.1f} больше на балкон не хочется "
                    f"выходить...\nЯ лучше полежу на белых чистых глаженных вещах хозяина ^_^")
    elif temp_yesterday < 0:
        text.append("В такую погоду стараюсь спать около батарей.")
        text.append(f"На улице холодно, брр... Хотелось бы +20, но завтра {temp_yesterday:.1f} градусов(")
        text.append(f"Сделала себе какао с молоком и смотрела на чудесный снегопад! "
                    f"Завтра вообще будет {temp_yesterday:.1f}, надо утепляться!")
        text.append(f"Прохладно завтра. На улице {temp_yesterday:.1f}, поэтому рыбку из пруда достать не удастся(")
    elif temp_yesterday < 10:
        text.append(
            f"Даже красная точка не выманит меня из дома. Завтра будет {temp_yesterday:.1f} градусов, но хотя бы"
            f" не зима и то хорошо.")
    elif temp_yesterday < 20:
        text.append(f"Солнышко иногда появляется, греюсь на подоконнике рядом с кошачей мятой.")
    elif temp_yesterday >= 20:
        text.append(f"Я счаслива, завтра будет моя самая любимая температура - {temp_yesterday:.1f}")

    temps = weather.get_weather(1)
    res = random.choice(text) + "\n\nТемпература на завтра:\nУтром: {}\nДнем: {}\nВечером: {}\nНочью: {}".format(*temps)

    return res


def joke():
    text = ["О, а я знаю один анекдот!", "Значит слушай...", "Без проблем!",
            "Ха-ха, как раз сегодня такую шутку прочитала:",
            "Мяу-мяу... А пототм как МЯУ! Ахахах, сейчас переведу шутку на человечий:"]
    res = random.choice(text) + "\n" + anektod.get_joke()
    return res


def joke_for_fish(fish):
    text = [f"Может за это ты мне пришлёшь {fish} эту рыбку?",
            f"За рыбку раскажу. А хочу я именно {fish}",
            f"Не хочу рассказывать анекдот.\nНу, если у тебя случайно не затерялась эта рыбка - {fish}"]
    res = random.choice(text)
    return res


def send_photo():
    text = ["Интересная картинка. Но у меня лучше)",
            "Продаешь? Нет? Только посмотреть? Красивое...",
            "А у меня есть фотка получше!"]
    return random.choice(text)


def subscribe():
    text = [f"Договорились ^_^\nВ будущем буду присылать тебе новости.",
            f"О, правда? Я очень интересуюсь этим)\nКак найду что-то интересное - пришлю",
            f"Записала тебя на курсы рыбалки. По средам в 5:30 будешь ловить вкусняшку и за это буду присылать "
            f"тебе классные посты😊",
            f"Записала тебя в специальный список"]
    res = random.choice(text)
    return res


def subscribe_exist():
    text = ["Уже-уже, не переживай)",
            "Так ты уже получаешь новости. Если подумаешь, что я забыла, то это ложь! Я всё помню!"]
    res = random.choice(text)
    return res


def unsubscribe():
    text = ["Принято, вычёркиваю!",
            "Вот и договорились, я сама немного отдохну =)"]
    res = random.choice(text)
    return res


def error():
    text = ["Ой... Что-то пошло не так.",
            "Похоже, что у меня лапки и я что-то сломала. Пока не могу это сделать("]
    res = random.choice(text)
    res = "❗️" + res
    return res


def perplexity():
    text = ["Нуу... Тебе видней.", "Ла-а-а-адно, как скажешь"]
    res = random.choice(text)
    return res


def add_section(sel=0, theme_name=None, datetime=None):
    """
    :param sel: Тип диалога:
    0 - Всё готово
    1 - Добавление названия
    2 - Добавление времени
    """
    if sel == 0:
        text = [f"Прекрасно, новая рубрика {theme_name} готова!", f"Новый раздел вопросов {theme_name} готов!"]
    elif sel == 1:
        text = ["Какую тему вопросов будем создавать?", "Как назовём новый раздел вопросов?"]
    elif sel == 2:
        text = ["Давай поставим сроки данной темы.",
                "Поставь время окончания данного раздела.\n__(Я его удалять пока не буду)__"]
    else:
        text = unknown_command()
    res = random.choice(text)
    if sel == 0 and datetime:
        res += f"\nВремя окончания рубрики: {datetime}"
    return res


def add_question(sel=0, theme_name=None, datetime=None):
    """
    :param sel: Тип диалога:
    0 - Всё готово
    1 - Группа вопроса
    2 - Добавление названия
    3 - Добавление ответа
    4 - Добавление короткого ответа
    """
    if sel == 0:
        text = [f"Вопрос добавлен!"]
    elif sel == 1:
        text = ["Какая рубрика вопроса?"]
    elif sel == 2:
        text = ["Давай поставим сроки данной темы.",
                "Поставь время окончания данного раздела.\n__(Я его удалять пока не буду)__"]
    else:
        text = unknown_command()
    res = random.choice(text)
    if sel == 0 and datetime:
        res += f"\nВремя окончания рубрики: {datetime}"
    return res
