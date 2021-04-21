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

    return_lines = ["Symbol:\tCurrent:\tStarting:\tChange:"]
    print_rows = []
    for symbol in original_prices:
        cp = current_prices[symbol]
        op = original_prices[symbol]
        print_rows.append((symbol, cp, op, ((cp - op)/op)*100))
    print_rows = sorted(print_rows, key=lambda x: -1*x[3])
    for (symbol, cp, op, change) in print_rows:
        return_lines.append(symbol + 
                            (' '*(11-len(symbol))) + "$" + '%.2f' % cp + 
                            (' '*(11-len('%.2f' % cp))) + "$" + '%.2f' % op +
                            (' '*(11-len('%.2f' % op))) + (" " if cp > op else "") + '%.2f' % change + "%")
    return "```\n" + '\n'.join(return_lines) + "```"

client.run(DISCORD_TOKEN)
