import discord
import random
import sys
import os
import dotenv
import time

dotenv.load_dotenv()

TOKEN = os.getenv('TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)
guessleft = 6
words = []
with open ('wo.txt','r') as f:
    words = [line.rstrip() for line in f]

common_words = []
with open ('wo.txt','r') as f:
    common_words = [line.rstrip() for line in f]

rw = random.choice(common_words)


def wcheck(l, p) ->str:
    global rw
    if rw[p] == l:
        return f"You got {l} in the right spot"
    elif l == rw[0] or l == rw[1] or l == rw[2] or l == rw[3] or l == rw[4]:
        return f"{l} is in the string, but not in this location"
    else:
        return f"The letter {l} does not exist in the word"


def realword(w) ->bool:
    global words
    if w in words:
        return True
    else:
        return False


@client.event
async def on_ready():

    general_channel = client.get_channel(int(CHANNEL_ID))

    await general_channel.send('Welcome to wordle, to play, use the command .p followed by the word you want to enter')

@client.event
async def on_message(message):
    if message.author == client.user:
        return  # Ignore messages sent by the bot itself

    global guessleft
    global rw
    general_channel = client.get_channel(int(CHANNEL_ID))
    await general_channel.send(f"test")
    time.sleep(1)
    # if len(message.content) >= 2 and message.content[0] == '.' and message.content[1] == 'p':
    #     try:
    #         guesslist = []
    #         guesslist.append(message.content[3])
    #         guesslist.append(message.content[4])
    #         guesslist.append(message.content[5])
    #         guesslist.append(message.content[6])
    #         guesslist.append(message.content[7])
    #         guess = "".join(guesslist)
    #     except:
    #         general_channel = client.get_channel(int(CHANNEL_ID))
    #         await general_channel.send(f"Please enter a word that is 5 characters long")



    #     if guess == rw and realword(guess):
    #         general_channel = client.get_channel(int(CHANNEL_ID))
    #         await general_channel.send(f"Holy You are Cracked, you got the right answer. The word is {rw}")
    #         guessleft = 6
    #         rw = random.choice(words)
    #     elif realword(guess):
    #         #if rightspotCheck(guess):
    #         general_channel = client.get_channel(int(CHANNEL_ID))
    #         await general_channel.send(wcheck(guess[0], 0))
    #         await general_channel.send(wcheck(guess[1], 1))
    #         await general_channel.send(wcheck(guess[2], 2))
    #         await general_channel.send(wcheck(guess[3], 3))
    #         await general_channel.send(wcheck(guess[4], 4))
    #         guessleft-=1
    #         await general_channel.send(f"You have {guessleft} guesses left")
    #     else:
    #         general_channel = client.get_channel(int(CHANNEL_ID))
    #         await general_channel.send(f"You entered an invalid word, try again, you still have {guessleft} guesses left")
        
    #     if guessleft == 0:
    #         general_channel = client.get_channel(int(CHANNEL_ID))
    #         await general_channel.send(f"Wow you suck, you couldn't even get the word {rw} right")
    #         guessleft = 6
    #         rw = random.choice(words)


client.run(TOKEN)