from interactions import slash_command, SlashContext, Client, slash_option, OptionType, auto_defer, listen
from interactions.models.discord.file import File
from io import BytesIO
from os import environ
from morshutalk.morshu import Morshu
import nltk
from time import time
nltk.download("averaged_perceptron_tagger_eng")

bot = Client(token=environ["BOT_TOKEN"])


@slash_command(name="morshu", description="make morshu say things", scopes=[353071720342487040])
@slash_option(name="text", description="the things", opt_type=OptionType.STRING)
async def cmd_morshu(ctx: SlashContext, text: str):
    morshu = Morshu()
    audio = morshu.load_text(text)
    f = BytesIO()
    audio.export(f, format="mp3")
    f = File(file=f, file_name=f"morshu{int(time())}.mp3")
    await ctx.send(file=f)

@listen()
async def on_startup():
    print("Bot started")

bot.start()
