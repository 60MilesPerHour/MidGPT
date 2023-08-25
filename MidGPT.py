import time
import discord
import openai
from discord.ext import commands
from dotenv import load_dotenv
import pyautogui as pg

# Load environment variables
load_dotenv()

# Fetch tokens from .env
discord_token = os.getenv("DISCORD_TOKEN")
openai_key = os.getenv("OPENAI_API_KEY")

def MidGPT():
    """
    Function to get a response from GPT-3 with a specific prompt.
    """
    openai.api_key = openai_key

    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "user", "content": "give me an /imagine prompt, in this case, /imagine will be used for an AI art generator, imagine something for the ai to generate in 10 words or less with medium detail (note: you can't used inappropriate words, or else the ai will not generate anything)"},
      ]
    )

    MidGPT_Response = completion.choices[0].message.content
    return MidGPT_Response

client = commands.Bot(command_prefix="*", intents=discord.Intents.all())

# Flag to control the automation
automation = False

@client.event
async def on_ready():
    """
    Event triggered when the bot is ready.
    """
    print("Bot connected")

@client.event
async def on_message(message):
    """
    Event triggered when a message is received.
    """
    global automation

    msg = message.content   
    print(message)

    # Start Automation by typing "automation" in the discord channel
    start_commands = ['automation', 'auto', 'start']
    if msg.lower() in start_commands:
        automation = True

    # Stop Automation by typing "stop" in the discord channel
    stop_commands = ['stop', 'end', 'end automation', 'stop automation']
    if msg.lower() in stop_commands:
        automation = False

    if automation:
        prompts = str(MidGPT())  # get the AI generated prompt
        time.sleep(3)
        pg.press('tab')
        time.sleep(3)
        pg.write('/imagine')
        time.sleep(5)
        pg.press('tab')
        pg.write(prompts)
        time.sleep(3)
        pg.press('enter')
        time.sleep(5)

        # Continue Automation as soon Midjourney bot sends a message with attachment.
        for attachment in message.attachments:
            prompts = str(MidGPT())  # get the AI generated prompt
            time.sleep(3)
            pg.write('/imagine')
            time.sleep(5)
            pg.press('tab')
            pg.write(prompts)
            time.sleep(3)
            pg.press('enter')
            time.sleep(5)

        # Wait for 90 seconds before starting the next job
        time.sleep(90)

# Run the bot
client.run(discord_token)
