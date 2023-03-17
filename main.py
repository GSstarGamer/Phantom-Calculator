import math
import argparse


def roundNum(number, place):
    return int(math.ceil(number / place)) * place


def nextReward(rank):
    return (rank*5)+200


def rankCredit(rank):
    credits = 0
    for i in range(rank):
        credits += nextReward(i)
    return credits


def reducedPrice(gunRank, currentRank):
    return 140*(gunRank - currentRank) + 700


def rankForgun(gunRank):  # No credits must be used inorder to get the gun

    possible = []
    for rank in range(300):
        if roundNum(rankCredit(rank), 1000) == roundNum(reducedPrice(gunRank, rank), 1000):
            possible.append(
                [rankCredit(rank), reducedPrice(gunRank, rank), rank])

    for poss in possible:
        if poss[0] >= poss[1]:
            return [poss[2], poss[1]]


def rankForXP(currentRank=0, rank=1):
    return (1000*(((currentRank**2) + currentRank)/2)) - (1000*(((rank**2) + rank)/2))


parser = argparse.ArgumentParser(description="PhantomisForced with maths",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)

group = parser.add_mutually_exclusive_group()

group.add_argument("-rC", "--rankCredit", type=int,
                   help="Gives amount of credits your supposed to get depending on rank.")

group.add_argument("-rP", "--reducedPrice",
                   type=lambda s: [int(item) for item in s.split(',')], help="Gives the reduced price depending on current rank. [GUNRANK,CURRENTRANK]")

group.add_argument("-nR", "--nextReward",
                   type=int, help="Amount of credits you will get next with given rank.")

group.add_argument("-rFg", "--rankForgun",
                   type=int, help="Gives the rank you need to prebuy a gun. NOTE: Must not use a single credit to give answer, and MVPs and skins are not included.")

group.add_argument("-rXP", "--rankForXP",
                   type=lambda s: [int(item) for item in s.split(',')], help="Amount of XP need to rank up to the level given. [RANK, CURRENTRANK(optional)]")

args = vars(parser.parse_args())


for arg, value in args.items():
    if value != None:

        if arg == 'rankCredit':
            print(
                f'You will get should {rankCredit(value)} credits from rank 0.')

        elif arg == 'reducedPrice':
            print(
                f'The reduced price is {reducedPrice(value[0], value[1])} for gun {value[0]}.')

        elif arg == 'nextReward':
            print(f'You will get {nextReward(value)} credits next rank.')

        elif arg == 'rankForgun':
            print(
                f'You need to be rank {rankForgun(value)[0]} to get {value} rank gun which is {rankForgun(value)[1]} credits.')
        elif arg == 'rankForXP':
            if len(value) > 1:
                currentRank = value[1]
            else:
                currentRank = 0
            
            print(f'You will need {rankForXP(currentRank, value[0])} for {value[0]}. Which is {rankForXP(currentRank, value[0])/100} kills without headshots.')
