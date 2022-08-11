from random import choice


def get_jokes(n, flag=False):
 for i in range(n):
    word_nouns = choice(nouns)
    word_adverbs = choice(adverbs)
    word_adjectives = choice(adjectives)
    joke = f'{word_nouns} {word_adverbs} {word_adjectives}'
    list_1 = []
    print(joke)
    if flag == True:
      list_1 = joke.split()
      for noun in nouns:
        for fun in list_1:
          if noun == fun:
            nouns.remove(noun)
            for adverb in adverbs:
              for fun in list_1:
                if adverb == fun:
                 adverbs.remove(adverb)
            for adjective in adjectives:
             for fun in list_1:
              if adjective == fun:
               adjectives.remove(adjective)


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

get_jokes(n=5, flag=True)