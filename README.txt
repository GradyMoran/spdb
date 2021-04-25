This is a discord bot to track the performance of a set of stocks. Early WIP

Installation instructions:
apt install python3-venv
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
Add the bot on discord side, and put the TOKEN in a file called .env with format like "DISCORD_TOKEN=<token>"
If you would like the bot to print out automatically to a channel when it receives sigusr1, add SIGNAL_PRINT_CHANNEL=<channel id> to .env. The channel id comes from right clicking the channel in the discord client and clicking "copy id"
Change the config.txt to represent the portfolio you want to track. The format is simply symbol,purchase_price, one per line. No spaces, comma separated, no blank lines, no comments.
(with virtual environment enabled) run the bot

Set up a cron to print the prices every weekday at noon:
0 12 * * 1,2,3,4,5 kill -10 $(ps -ef | grep 'python spdb.py' | grep -v grep | awk '{ print $2 }')
