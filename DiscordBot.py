import os
import discord
from discord.ext import commands
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

#Gemini-----------------------------------------------------------------------
#see .env file 
gemini_api_key = os.getenv('GEMINI_API_KEY') 
genai.configure(api_key=gemini_api_key)

generation_config = {
    "temperature": 1.,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)
#Discord Bot----------------------------------------------------------------
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='!')
async def ask(ctx, *, question):
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(question)
    await ctx.send(response.text)

discord_bot_token = os.getenv('DISCORD_BOT_TOKEN')
bot.run(discord_bot_token)
#first post yaay
