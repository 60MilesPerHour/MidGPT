## README.md for Midjourney Art Generator Automation using ChatGPT

---

### Introduction

This bot automates the generation of `/imagine` prompts using ChatGPT, which are then used for the Midjourney Art generator on Discord.

---

### Dependencies

1. `discord.py`: A modern, easy-to-use Python wrapper for the Discord API.
2. `openai`: The official OpenAI Python client, which allows you to directly interact with the GPT models.
3. `python-dotenv`: Allows you to load environment variables from a `.env` file.
4. `pyautogui`: Allows you to programmatically control the mouse & keyboard.

---

### Setup and Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/60MilesPerHour/MidGPT/tree/24f0a68e0c341a6a923111a2a9213beebb337382
    ```

2. Navigate to the directory:
    ```bash
    cd [MidGPT](https://github.com/60MilesPerHour/MidGPT/tree/24f0a68e0c341a6a923111a2a9213beebb337382)
    ```

3. Install the dependencies:
    ```bash
    pip install discord.py openai python-dotenv pyautogui
    ```

4. Create a `.env` file in the root directory of your project and add your Discord bot token and OpenAI API key:

    ```
    DISCORD_TOKEN=YOUR_DISCORD_TOKEN
    OPENAI_API_KEY=YOUR_OPENAI_API_KEY
    ```

    Replace `YOUR_DISCORD_TOKEN` and `YOUR_OPENAI_API_KEY` with your actual tokens.

---

### Creating a Discord Bot

1. Navigate to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click on the "New Application" button and give your application a name.
3. Go to the "Bot" tab on the left side and click on "Add Bot".
4. Under the TOKEN section, click on "Copy" to copy your bot token. (This is what you'll paste into the `.env` file for `DISCORD_TOKEN`).
5. Invite your bot to your server by going to the "OAuth2" tab, checking the `bot` box under `scopes`, and then selecting the permissions your bot needs under `BOT PERMISSIONS`. Use the generated link to add your bot to a server.

For a detailed guide on setting up a Discord bot, you can follow this [guide](https://discordpy.readthedocs.io/en/stable/discord.html).

---

### Running the Bot

1. Once everything is set up, run the bot using:
    ```bash
    python MidGPT.py
    ```

2. Once the bot is running, you can use the automation features within your Discord server.

---

### Notes

- Always keep your tokens private. Never expose your Discord or OpenAI API tokens in public repositories or forums.
- Ensure that you handle errors and edge cases for a more robust application, especially if planning to scale or use in a production setting.

---

I hope this README helps you in setting up and understanding the bot! If you have any issues, please refer to the official documentation of each dependency or reach out to their respective communities.
