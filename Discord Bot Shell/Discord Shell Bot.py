import discord
import subprocess
import threading
import asyncio

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Initialize a list to store the shell output
output = []

# Function to read output from the shell
def read_output(pipe):
    global output
    for line in iter(pipe.readline, ""):
        output.append(line.strip())

# Start a Bash shell subprocess
shell = subprocess.Popen(
    ["bash"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    universal_newlines=True)

# Create threads to read stdout and stderr
stdout_thread = threading.Thread(target=read_output, args=(shell.stdout,))
stderr_thread = threading.Thread(target=read_output, args=(shell.stderr,))
stdout_thread.start()
stderr_thread.start()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$'):
        global output

        command = message.content[1:]
        
        # Send the command to the shell
        shell.stdin.write(command + "\n")
        shell.stdin.flush()
        
        # Wait for the shell to process the command (adjust sleep time as needed)
        await asyncio.sleep(1)
        
        # Get the output from the shell and format it
        temp_output = " \n".join(output)
        
        # Send the formatted output back to the Discord channel
        await message.channel.send(f"```\n{temp_output}\n```")
        
        # Clear the output buffer
        output.clear()

# Replace 'YOUR_BOT_TOKEN' with your actual Discord bot token
client.run('YOUR_BOT_TOKEN')
