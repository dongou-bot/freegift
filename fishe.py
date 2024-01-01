import discord
import random
from discord.ext import commands

# 봇 설정
bot = commands.Bot(command_prefix='!')

# 낚시 명령어 구현
@bot.command(name='낚시')
async def fishing(ctx):
    fishes = ['고래', '상어', '개복치', '참치', '문어', '오징어', '낙지', '게', '명태']
    selected_fish = random.choice(fishes)
    await ctx.send(f'{ctx.author.mention}, 낚은 물고기: {selected_fish}')

# 봇 실행
bot.run('YOUR_BOT_TOKEN')
