# for madlibs Game with get some name, fName, Adj, verb
exc = (input("Enter a exclamation: "))
adv = (input("Enter a adverb: "))
noun = (input("Enter a noun: "))
adj = input("Enter a adjective: ")

sentence = (f"{exc}! he said {adv} as he jumped into his convertible {noun} and drove off with his {adj} wife.")

print(sentence)

# know we want to auto generate thease input
from sample_madlibs import hp, code, zombies, hungergames
import random
# we should have some file that have that specifie object for our sentence

if __name__ == "__main__":
    m = random.choice([hp, code, zombies, hungergames])
    m.madlib()