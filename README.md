# CartmanGPT Discord Bot

A simple Discord bot using the CartmanGPT package from [Steamship](https://www.steamship.com/) to generate fun responses as Eric Cartman when mentioned.

## Prerequisites

- Python 3.6 or higher
- A Discord bot token. Create a Discord bot and obtain its token from the [Discord Developer Portal](https://discord.com/developers/applications).
- Steamship instance handle for the CartmanGPT model. You can create an instance [here](https://www.steamship.com/packages/cartmangpt).
- Steamship API Key. Authenticate with Steamship using the `ship login` command.

## Authentication

Steamship uses API Keys to authenticate the CLI and client libraries. These keys can be stored in a configuration file, in environment variables, or passed manually to the client libraries.

Steamship Configuration File:
Logging in with the Steamship CLI creates a configuration file at `~/.steamship.json`. This file contains your API Key, and the client libraries will auto-load information from this file when available.

The configuration file should look like this:

```
{
  "apiKey": "mykey"
}
```

## Installation

### Normal Setup

1. Clone this repository:

```bash
git clone https://github.com/yourusername/cartmangpt-discord-bot.git
cd cartmangpt-discord-bot
```

2. Authenticate with Steamship by running the following command and providing your API key:

```bash
ship login
```

3. Install the required Python packages:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project folder with the following content:

```
INSTANCE_HANDLE=your-instance-handle
DISCORD_BOT_TOKEN=your-discord-bot-token
```

Replace `your-instance-handle` and `your-discord-bot-token` with the actual values.

### Replit Setup

1. Fork this repository and import it into [Replit](https://replit.com/), or fork the Replit template [here](https://replit.com/@Honkware/Steamship-CartmanGPT-Discord-Bot).

2. In Replit, click on the "Secrets" tab (lock icon) and add the following environment variables:

- INSTANCE_HANDLE: your-instance-handle
- DISCORD_BOT_TOKEN: your-discord-bot-token
- STEAMSHIP_API_KEY: your-steamship-api-key

Replace `your-instance-handle`, `your-discord-bot-token`, and `your-steamship-api-key` with the actual values.

3. Authenticate with Steamship by running the following command in the Replit shell and providing your API key:

```bash
ship login
```

4. Install the required Python packages by running the following command in the Replit shell:

```bash
pip install -r requirements.txt
```

## Running the Bot

To run the bot, simply execute the following command in your terminal, command prompt, or Replit:

```bash
python bot.py
```

The bot will log in to Discord, and you should see the message `We have logged in as {client.user}`. The bot will now respond to mentions in the server it's connected to.
