import discord
import subprocess
import threading
import asyncio
import importlib.util
import sys
import platform

# Check if discord module is installed, if not, install it
try:
    importlib.util.find_spec('discord')
except ImportError:
    print("discord module not found. Installing...")
    if platform.system() == "Windows":
        subprocess.check_call([sys.executable, "-m", "pip", "install", "discord.py"])
    else:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "discord"])
    importlib.reload(discord)

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

output = []

def read_output(pipe):
    global output
    for line in iter(pipe.readline, ""):
        output.append(line.strip())

if platform.system() == "Windows":
    shell = subprocess.Popen(
        ["cmd"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        universal_newlines=True,
        bufsize=1,
        creationflags=subprocess.CREATE_NEW_PROCESS_GROUP
    )
else:
    shell = subprocess.Popen(
        ["bash"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        universal_newlines=True
    )

stdout_thread = threading.Thread(target=read_output, args=(shell.stdout,))
stderr_thread = threading.Thread(target=read_output, args=(shell.stderr,))
stdout_thread.start()
stderr_thread.start()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$'):
        global output
        command = message.content[1:]
        if command == 'host':
            await message.channel.send(f"The bot is currently running on {platform.system()}.")
        else:
            shell.stdin.write(command + "\n")
            shell.stdin.flush()
            await asyncio.sleep(1)
            temp_output = " \n".join(output)
            await message.channel.send(f"```\n{temp_output}\n```")
            output.clear()

client.run('YOUR_BOT_TOKEN')
