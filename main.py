from random import randint

random_replies = [
    "Oh wirklich?",
    "Sind Sie sich dessen sicher?",
    "Hmmmm.",
    "Interessant...",
    "Ich weiß nicht recht, ob ich da Ihrer Meinung bin...",
    "Definitiv",
    "Vielleicht!",
    "Und was genau wollen Sie damit sagen?",
    "Und das heißt was?",
    "Stimmt wohl.",
    "Unsinn! Völliger Unsinn!",
    "Und, was haben Sie morgen vor?",
    "Ich habe gerade genau dasselbe gedacht.",
    "Das ist wohl eine verbreitete Meinung.",
    "Eine Menge Leute haben das gesagt.",
    "Wunderbar!",
    "Das könnte ein wenig peinlich werden!",
    "Glauben Sie das wirklich?",
    "Tatsächlich...",
    "Genau was ich sage!",
    "Ich verstehe..."]

chat_dictry = {
    "glücklich": "Ich bin heute auch gut drauf!",
    "traurig": "Kopf hoch, Genosse!",
    "himbeere": "Lecker! Ich mag Himbeeren!",
    "computer": "Rechner an die Macht!, Sie sprechen schon mit einem.",
    "musik": "Haben Sie das neue Album von Lana Del Rey gehört?",
    "kunst": "Mal ehrlich, was ist denn Kunst überhaupt?",
    "witz": "Treffen sich zwei Jäger im Wald.",
    "python": "Ich wurde in dieser Programmiersprache programmiert ^^",
    "dummkopf": "Du nennst mich Dummkopf, Matschbirne?",
    "wetter": "Ich frage mich, ob es Samstag sonnig wird?",
    "sie": "Halten Sie mich daraus!",
    "sicher": "Wie können Sie sich dessen so sicher sein?",
    "reden": "Immer nur labern! Handeln!",
    "denken": "Sie können das ja mal überschlafen.",
    "hallo": "Hallo! Alles klar in Sansibar?",
    "kosten": "Nichts ist kostenlos. Selbst der Tod kostet das Leben.",
    "bye": "Bis später ;D"}


def dictionary_check(message):
    message = message.lower()
    user_words = message.split()
    smart_replies = []
    for each_word in user_words:
        if each_word in chat_dictry:
            answer = chat_dictry[each_word]
            smart_replies.append(answer)
    if smart_replies:
        reply_selected = randint(0, len(smart_replies))-1
        return smart_replies[reply_selected]
    else:
        return ""


user_says = ""

while user_says != "Bye":

    user_says = ""
    while user_says == "":
        user_says = input("Du: ")
    smart_response = dictionary_check(user_says)
    if smart_response:
        print("Kian:", smart_response)
    else:
        reply_chosen = randint(0, len(random_replies))-1
        print("Kian:", random_replies[reply_chosen])
        random_replies[reply_chosen] = user_says

print("Die Kommunikation wurde beendet.")
