
import random
templets=int(input('Please chose temlets 1 , 2, or 3: '))
numbers=input('Enter 2 numbers: ')
numbers=numbers.split()
number=random.shuffle(numbers)
names=input('Enter a name: ')
adjectives=input('Enter 5 adjectives: ')
adjectives=adjectives.split()
adjective=random.shuffle(adjectives)
nouns=input('Enter 5 nouns: ')
nouns=nouns.split()
noun=random.shuffle(nouns)
measure_of_times=input('Enter a measure of time: ')
colors=input('Enter 2 color: ')
colors=colors.split()
color=random.shuffle(colors)
verbs=input('Enter 2 verb: ')
verbs=verbs.split()
verb=random.shuffle(verbs)
animals=input('Enter 2 animals: ')
animals=animals.split()
animal=random.shuffle(animals)
silly_words=input('Enter 2 silly word: ')
silly_words=silly_words.split()
silly_word=random.shuffle(silly_words)
verb_ing=input('Enter verb +ing: ')

if templets==1:
  mode_of_transportation=input('Enter mode of transportation: ')
  part_of_the_bodes=input('Enter 2 part of body: ')
  part_of_the_bodes=part_of_the_bodes.split()
  part_of_the_body=random.shuffle(part_of_the_bodes)
  print()
  print('It was about', numbers[0], measure_of_times[0], 'ago when I arrived at the hospital in a', mode_of_transportation,'. The hospital is a/an',adjectives[0],' place, there are a lot of', adjectives[1], nouns[0],'here. \n There are nurses here who have', colors[0], part_of_the_bodes[0],'. If someone wants to come into my room I told them that they have to', verbs[0], ' first.\n I have decorated my room with', numbers[1], nouns[1],'. Today I talked to a doctor and they were wearing a',nouns[2],'. on their', part_of_the_bodes[1],'.\n I heard that all doctors', verbs[1], nouns[3],' every day for breakfast. The most',adjectives[2],' thing about being in the hospital is the', silly_words[0], nouns[4],'!')
elif templets==2:
  adverb=input('Enter adverb (ending in ly): ')
  adjectives_fill=input('Enter 2 adjectives(filling): ')
  adjectives_fill=adjectives_fill.split()
  adjective_fill=random.shuffle(adjectives_fill)
  print()
  print('This weekend I am going camping with', names, '. I packed my lantern, sleeping bag, and', nouns[0], '.\nI am so', adjectives_fill[0],' to', verbs[0],' in a tent. I am ',adjectives_fill[1],'we might see a(n)', animals[0],'\nI hear they are kind of dangerous. While we are camping, we are going to hike, fish, and', verbs[1], '.\nI have heard that the', colors[0], ' lake is great for', verb_ing,'. Then we will',adverb,' hike through the forest for', numbers[0], measure_of_times[0], '.\nIf I see a', colors[1], animals[1],' while hiking, I am going to bring it home as a pet!\nAt night we will tell',numbers[1], silly_words[0], 'stories and roast', nouns[1],' around the campfire!!')
else:
  place=input('Enter a place: ')
  magical_creaturs=input('Enter 2 Magical Creature (Plural):  ')
  magical_creaturs=magical_creaturs.split()
  magical_creatur=random.shuffle(magical_creaturs)
  room=input('Enter room in house: ')
  nouns_plu=input('Enter 2 nouns plural: ')
  nouns_plu=nouns_plu.split()
  noun_plu=random.shuffle(nouns_plu)
  print()
  print('Dear', names,', I am writing to you from a', adjectives[0], 'castle in an enchanted forest.\nI found myself here one day after going for a ride on a', colors[0], animals[0],' in', place, '.\nThere are', adjectives[1], magical_creaturs[0], 'and', adjectives[2], magical_creaturs[1],' here! In the', room,'there is a pool full of', nouns[0],'.\nI fall asleep each night on a', nouns[1], ' of', nouns_plu[0],' and dream of', adjectives[3], nouns_plu[1], '. \nIt feels as though I have lived here for', numbers[0], measure_of_times,'.\nI hope one day you can visit, although the only way to get here now is', verb_ing,'on a', adjectives[4], nouns[4],'!!')
