meme_expl = {
    "лол": "очень смешно",
    "кринж": "что-то странное, стыдное",
    "рофл": "шутка",
    "щищ": "одобрение или восторг",
    "криповый":  "страшный, пугающий",
    "агриться": "злиться"
    }

for i in range(5):
    word_req = input("Input word that you want an explanation")
    if word_req in meme_expl.keys():
        print("значит " + meme_expl[word_req])
    else:
        print("word not in database")
