# Discord Shell Bot

## Description
This script serves as a Discord bot designed to facilitate live interaction between a Discord server and a Bash shell. Users can initiate commands in Bash or Command Prompt format by prefixing them with a "$" symbol within their messages. The bot then executes these commands within a subprocessed shell, capturing both standard output and error streams. Results are formatted and relayed back to the Discord channel as messages.

## Features
- Monitors messages within a Discord server.
- Executes Bash and Command Prompt commands initiated by users prefixed with "$".
- Captures and formats standard output and errors from the shell.
- Relays output back to the Discord channel for user viewing.
- Facilitates live interaction with a Bash shell via Discord.
- Compatible with both Windows and Linux environments.

## Usage
1. Invite the bot to your Discord server.
2. Prefix Bash commands with "$" to execute them through the bot.
3. The bot will respond with the output of the command, formatted within triple backticks ("```") for readability.

**Note:** Make sure to insert your Discord bot token where indicated for the `client.run('')` line to enable your bot to connect to your server.

## Disclaimer
Please use this bot responsibly and only in environments where you have appropriate permissions. Unauthorized or malicious use of this bot may violate Discord's terms of service and result in sanctions.
