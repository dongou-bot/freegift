import discord
import random
from discord.ext import commands

token = ''

bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())

current_word = ""
used_words = set()

# 대기열을 저장할 딕셔너리
gift_queues = {}

@bot.event
async def on_ready():
    print(f"{bot.user.name}이(가) 성공적으로 로그인했습니다!")

@bot.command()
async def 안녕(ctx):
    await ctx.send('안녕하세요!')

@bot.command(name="giftmake")
async def make(ctx, queue_name):
    gift_queues[queue_name] = []
    await ctx.send(f'`{queue_name}` 추첨이 시작되었습니다.')

@bot.command(name="giftjoin")
async def join(ctx, queue_name):
    # 대기열에 사용자 추가
    if queue_name in gift_queues:
        user = ctx.message.author
        gift_queues[queue_name].append(user)
        await ctx.send(f'{user.mention} 님 `{queue_name}` 추첨에 참여하셨습니다.')
        print(gift_queues)
    else:
        await ctx.send(f'`{queue_name}` 대기열이 존재하지 않습니다.')

@bot.command(name="giftdone")
async def done(ctx, queue_name):
    # 대기열에서 한 명의 사용자 무작위로 선택하고 메시지로 알림
    if queue_name in gift_queues and gift_queues[queue_name]:
        winner = random.choice(gift_queues[queue_name])
        await ctx.send(f'당첨자는 {winner.mention} 님 축하드립니다.')
        # 대기열 비우기
        gift_queues[queue_name] = []
    else:
        await ctx.send(f'`{queue_name}` 대기열이 비어있거나 존재하지 않습니다.')

# 낚시 명령어 구현
@bot.command(name='낚시')
async def fishing(ctx):
    fishes = ['고래', '상어', '개복치', '참치', '문어', '오징어', '낙지', '게', '명태']
    selected_fish = random.choice(fishes)
    await ctx.send(f'{ctx.author.mention}, 낚은 물고기: {selected_fish}')

@bot.command(name='끝말잇기', help='끝말잇기를 시작합니다.')
async def start_game(ctx):
    global current_word
    global used_words

    current_word = ""
    used_words = set()

    await ctx.send("끝말잇기를 시작합니다. 단어를 입력하세요!")

@bot.command(name='단어', help='단어를 입력하여 끝말잇기에 참여합니다.')
async def submit_word(ctx, word):
    global current_word
    global used_words

    if not current_word or (current_word and current_word[-1] == word[0] and word not in used_words):
        current_word = word
        used_words.add(word)
        await ctx.send(f"'{word}'를 제출했습니다. 다음 단어는 '{current_word[-1]}'로 시작해야 합니다.")
    else:
        await ctx.send("잘못된 단어입니다. 다시 시도해주세요.")


@bot.event
async def on_message(message):
    if message.author == bot.user:  # 봇이 보낸 메시지는 무시
        return

    if message.content.startswith("안녕"):
        user_mention = message.author.mention
        response = f'{user_mention} 님 안녕하세요!'
        await message.channel.send(response)

    await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("존재하지 않는 명령어입니다.")
    else:
        print(error)

bot.run(token)
