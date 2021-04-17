import discord
from dotenv import load_dotenv
import os
import yfinance

config_filename = "config.txt"

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client()

@client.event
async def on_ready():
    print(str(client.user) + "has connected to Discord!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "+portfolio":
        await message.channel.send(prices_printout())

def prices_printout():
    lines = []
    with open(config_filename) as f:
        lines = f.readlines()
    original_prices = {}
    for line in lines:
        original_prices[line.split(',')[0]] = float(line.split(',')[1])
    current_prices = {}
    for symbol in original_prices:
        current_prices[symbol] = yfinance.Ticker(symbol).info['regularMarketPrice']

    return_lines = ["\nSymbol:\tStarting:\tCurrent:\tChange:"]
    for symbol in original_prices:
        return_lines.append(symbol + "\t" + 
                            "$" + str(original_prices[symbol]) + "\t" + 
                            "$" + str(current_prices[symbol]) + "\t" +
                            '%.3f' % (((current_prices[symbol] - original_prices[symbol])/original_prices[symbol])*100) + "%")
    return '\n'.join(return_lines)

client.run(DISCORD_TOKEN)
