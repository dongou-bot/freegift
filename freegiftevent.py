import discord
from discord.ext import commands
import random

token = ''

bot = commands.Bot(command_prefix='.gift ', intents=discord.Intents.all())

# 대기열을 저장할 딕셔너리
gift_queues = {}

@bot.event
async def on_ready():
    print(f"{bot.user.name}이(가) 성공적으로 로그인했습니다!")

@bot.command()
async def 안녕(ctx):
    await ctx.send('안녕하세요!')

@bot.command(name="make")
async def make(ctx, queue_name):
    gift_queues[queue_name] = []
    await ctx.send(f'`{queue_name}` 추첨이 시작되었습니다.')

@bot.command(name="join")
async def join(ctx, queue_name):
    # 대기열에 사용자 추가
    if queue_name in gift_queues:
        user = ctx.message.author
        gift_queues[queue_name].append(user)
        await ctx.send(f'{user.mention} 님 `{queue_name}` 추첨에 참여하셨습니다.')
        print(gift_queues)
    else:
        await ctx.send(f'`{queue_name}` 대기열이 존재하지 않습니다.')

@bot.command(name="done")
async def done(ctx, queue_name):
    # 대기열에서 한 명의 사용자 무작위로 선택하고 메시지로 알림
    if queue_name in gift_queues and gift_queues[queue_name]:
        winner = random.choice(gift_queues[queue_name])
        await ctx.send(f'당첨자는 {winner.mention} 님 축하드립니다.')
        # 대기열 비우기
        gift_queues[queue_name] = []
    else:
        await ctx.send(f'`{queue_name}` 대기열이 비어있거나 존재하지 않습니다.')

@bot.event
async def on_message(message):
    if message.author == bot.user:  # 봇이 보낸 메시지는 무시
        return

    if message.content.startswith("안녕"):
        user_mention = message.author.mention
        response = f'{user_mention} 님 안녕하세요!'
        await message.channel.send(response)

    await bot.process_commands(message)

bot.run(token)
