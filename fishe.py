import discord
import random
from discord.ext import commands

# ë´ ì¤ì 
bot = commands.Bot(command_prefix='!')

# ëì ëªë ¹ì´ êµ¬í
@bot.command(name='ëì')
async def fishing(ctx):
    fishes = ['ê³ ë', 'ìì´', 'ê°ë³µì¹', 'ì°¸ì¹', 'ë¬¸ì´', 'ì¤ì§ì´', 'ëì§', 'ê²', 'ëªí']
    selected_fish = random.choice(fishes)
    await ctx.send(f'{ctx.author.mention}, ëì ë¬¼ê³ ê¸°: {selected_fish}')

# ë´ ì¤í
bot.run('YOUR_BOT_TOKEN')