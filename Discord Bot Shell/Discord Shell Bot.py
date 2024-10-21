import subprocess
import threading
import platform
MAX_RESPONSE_LENGTH = 1980

try:
    import discord
    import asyncio
except ImportError:
    import subprocess
    subprocess.run(['pip', 'install', 'discord.py', 'asyncio'], check=True)
    import discord
    import asyncio

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

output = []

def read_output(pipe):
    global output
    for line in iter(pipe.readline, ""):
        output.append(line.strip())

def create_shell():
    if platform.system() == "Windows":
        return subprocess.Popen(
            ["cmd"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            universal_newlines=True,
            bufsize=1,
            creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
    else:
        return subprocess.Popen(
            ["bash"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            universal_newlines=True)

shell = create_shell()

stdout_thread = threading.Thread(target=read_output, args=(shell.stdout,))
stderr_thread = threading.Thread(target=read_output, args=(shell.stderr,))
stdout_thread.start()
stderr_thread.start()

@client.event
async def on_message(message):
    global shell, output
    if message.author == client.user:
        return

    if message.content.startswith('$'):
        command = message.content[1:]
        if command == 'host':
            await message.channel.send(f"The bot is currently running on {platform.system()}.")
        else:
            shell.stdin.write(command + "\n")
            shell.stdin.flush()
            await asyncio.sleep(1)
            temp_output = " \n".join(output)
            output.clear()

            # Split the output into chunks of MAX_RESPONSE_LENGTH characters or less
            for i in range(0, len(temp_output), MAX_RESPONSE_LENGTH):
                chunk = temp_output[i:i + MAX_RESPONSE_LENGTH]
                await message.channel.send(f"```\n{chunk}\n```")

client.run('<your bot token')
