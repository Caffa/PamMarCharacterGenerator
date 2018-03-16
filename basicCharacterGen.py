import random, json

def NameGen():
    '''Generates a name (first & middle)'''
    with open("first-names.json", "r") as f:
        fname = json.load(f)

    with open("middle-names.json", "r") as c:
        mname = json.load(c)

    return "Name: " + random.choice(fname) + " " + random.choice(mname)





def StatGen():
    '''Generates all stats with values from 1 to 10'''
    listoStat = ["Strength", "Vitality", "Dexterity", "Endurance", "Intelligence", "Wisdom", "Charisma", "Agility"]
    s = ""
    for i in listoStat:
        a = str(random.randint(1,10))
        s += i + ": " + a +"\n"

    return s


def BasicPersonalityTraits():
    '''Generates the basic personality'''
    c = ["INTJ Architect", "INTP Logician", "ENTJ Commander", "ENTP Debater ", "INFJ Advocate", "INFP Mediator", "ENFJ Protagonist", "ENFP Campaigner", "ISTJ Logistician", "ISFJ Defender", "ESTJ Executive", "ESFJ Consul", "ISTP Virtuoso", "ISFP Adventurer", "ESTP Entrepreneur", "ESFP Entertainer"]
    s = "Personality: " + random.choice(c)

    return s

def sentenceGen(Nos, endRange):
    '''takes in the input of name of stat and range of stat assume one'''
    return Nos + ": " + str(random.randint(1,endRange))

def otherStats():
    age = sentenceGen("Age", 80)
    return age






def CharacterGen():
    '''Add functions here to compile basic character sheet'''
    name = NameGen()
    stat = StatGen()
    personality = BasicPersonalityTraits()
    oa = otherStats()
    return "Basic Stats: ---------------- \n\n" + name + "\n" + stat + personality + "\nOther Stats:  ----------------  \n\n" + oa
    # return "Basic Stats: \n" + name + "\n" + stat + personality

print(CharacterGen())
