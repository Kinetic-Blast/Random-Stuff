# Discord Shell Bot

## Description
This script is a Discord bot designed to create a live interaction between a Discord server and a Bash shell. It allows users to send Bash commands as messages starting with a "$" symbol, and the bot will execute these commands in a subprocessed Bash shell. The bot then captures the standard output and error streams of the shell and sends the results back to the Discord channel as formatted messages.

## Features
- Listens for messages in a Discord server.
- Executes Bash commands provided by users starting with "$".
- Captures and formats the standard output and error from the Bash shell.
- Sends the output back to the Discord channel for users to view.
- Provides a live interaction with a Bash shell via Discord.

## Usage
1. Invite the bot to your Discord server.
2. Prefix Bash commands with "$" to execute them through the bot.
3. The bot will respond with the output of the command, formatted within triple backticks ("```") for readability.

**Note:** Make sure to insert your Discord bot token where indicated for the `client.run('')` line to enable your bot to connect to your server.

## Disclaimer
Please use this bot responsibly and only in environments where you have appropriate permissions. Unauthorized or malicious use of this bot may violate Discord's terms of service and result in sanctions.
