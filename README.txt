This is a discord bot to track the performance of a set of stocks. Early WIP

Installation instructions:
apt install python3-venv
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
add the bot on discord side, and put the TOKEN in a file called .env with format like "DISCORD_TOKEN=<token>"
Change the config.txt to represent the portfolio you want to track. The format is simply symbol,purchase_price, one per line. No spaces, comma separated, no blank lines, no comments.
(with virtual environment enabled) run the bot
