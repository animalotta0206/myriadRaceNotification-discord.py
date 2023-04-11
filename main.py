import discord
import pytz
import datetime
import asyncio
import pnr2
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option
from discord.ext import commands
from discord.ext import tasks

client = discord.Client()
slash = SlashCommand(client, sync_commands=True)
jst = pytz.timezone('Asia/Tokyo')
date = datetime.datetime.now(jst)
weekday = date.weekday()
day = str(date.day)
month = str(date.month)
send_time = datetime.time(hour=9, minute=00)


async def calculate_next_send_time():
    """次にメッセージを送信するべき日時を計算"""
    now = datetime.datetime.utcnow()
    today_send_time = datetime.datetime.combine(now.date(), send_time)
    if today_send_time <= now:
        # 今日の送信時刻が過ぎている場合は、明日の同じ時刻に送信する
        next_send_time = datetime.datetime.combine(now.date() + datetime.timedelta(days=1), send_time)
    else:
        # 今日の送信時刻がまだ来ている場合は、今日の同じ時刻に送信する
        next_send_time = today_send_time
    return next_send_time
    
@tasks.loop()
async def send_message():
    """定期的にメッセージを送信"""
    next_send_time = await calculate_next_send_time()
    delta = next_send_time - datetime.datetime.utcnow()
    await asyncio.sleep(delta.total_seconds())
    channel = discord.utils.get(client.get_all_channels(), name='ミリアドゲーム告知')
    if weekday == 0:
     embed=discord.Embed(title="今日のミリアド開催時刻は…", color=0xe8f906)
     embed.add_field(name="開催時刻", value=f"ミリアドJPゲーム: {month}/{day} - 20:00", inline=False)
     await channel.send(embed=embed)
    elif weekday == 1:
     embed=discord.Embed(title="今日のミリアド開催時刻は…", color=0xe8f906)
     embed.add_field(name="開催時刻", value=f"ミリアドレース: {month}/{day} - 18:00〜18:25", inline=False)
     embed.add_field(name="対象ゲーム", value="パトルプッシャープレゼンス\nパトルプッシャーリアライズ\nトリプレットシャワー\nスカイドリーム\nスフィードパラダイス\nパスロット\nパトルーレット", inline=False)
     await channel.send(embed=embed)
    elif weekday == 2:
     embed=discord.Embed(title="今日のミリアド開催時刻は…", color=0xe8f906)
     embed.add_field(name="開催時刻", value=f"ミリアドJPゲーム: {month}/{day} - 21:00", inline=False)
     await channel.send(embed=embed)
    elif weekday == 3:
     embed=discord.Embed(title="今日のミリアド開催時刻は…", color=0xe8f906)
     embed.add_field(name="開催時刻", value=f"ミリアドレース: {month}/{day} - 20:00〜20:25", inline=False)
     embed.add_field(name="対象ゲーム", value="パトルプッシャープレゼンス\nパトルプッシャーリアライズ\nトリプレットシャワー\nスカイドリーム\nスフィードパラダイス\nブラックジャック\nフルーツチェイン", inline=False)
     await channel.send(embed=embed)
    elif weekday == 4:
     embed=discord.Embed(title="今日のミリアド開催時刻は…", color=0xe8f906)
     embed.add_field(name="開催時刻", value=f"ミリアドJPゲーム: {month}/{day} - 22:00", inline=False)
     await channel.send(embed=embed)
    elif weekday == 5:
     embed=discord.Embed(title="今日のミリアド開催時刻は…", color=0xe8f906)
     embed.add_field(name="開催時刻", value=f"ミリアドJPゲーム: {month}/{day} - 20:00\nミリアドレース: {month}/{day} - 20:30〜20:55", inline=False)
     embed.add_field(name="対象ゲーム", value="パトルプッシャープレゼンス\nパトルプッシャーリアライズ\nトリプレットシャワー\nスカイドリーム\nスフィードパラダイス\nパスロット\nパトルーレット", inline=False)
     await channel.send(embed=embed)
    elif weekday == 6:
     embed=discord.Embed(title="今日のミリアド開催時刻は…", color=0xe8f906)
     embed.add_field(name="開催時刻", value=f"ミリアドJPゲーム: {month}/{day} - 21:00\nミリアドレース: {month}/{day} - 21:30〜21:55", inline=False)
     embed.add_field(name="対象ゲーム", value="パトルプッシャープレゼンス\nパトルプッシャーリアライズ\nトリプレットシャワー\nスカイドリーム\nスフィードパラダイス\nブラックジャック\nフルーツチェイン", inline=False)
     await channel.send(embed=embed)

@slash.slash(name="help", description="botのヘルプを表示します")
async def help(ctx: SlashContext):
    embed=discord.Embed(title="bot-help", description="ミリアドJPゲーム・レースを告知するbotです。\r基本的にこのbotはスラッシュコマンドからの動作になります。",color=0x00ff00)
    embed.add_field(name="ミリアドレース定期告知", value="サーバーのどこかに「ミリアド告知」という名前のチャンネルを作成すると、毎日15時にミリアドゲームの告知が始まります。", inline=False)
    embed.add_field(name="サポートサーバーのご案内", value="サポートサーバーでは、製作者に直接お問い合わせすることができます。\n[サポートサーバーに参加](https://discord.gg/pFgBSt6MPX)", inline=False)
    await ctx.send(embed=embed)

@slash.slash(name="pnr2_myriad", description="パトネットリゾート2のミリアドまでの時間を取得します。")
async def pnr2_myriad(ctx: SlashContext):
    await pnr2.get_myriad(ctx)
 
#@slash.slash(name="pnr2_event", description="現在、パトネットリゾート2で開催中のイベントを取得します。")
#async def pnr2_event(ctx: SlashContext):
  #await pnr2.get_event(ctx)

@client.event
async def on_ready():
    send_message.start()
    game = discord.Game(f'Patnet Resort 2 [Casino / Coin Pusher]')
    await client.change_presence(status=discord.Status.online, activity=game)
    print('ログインしました')
    print('------')
    print(client.user.name)  # Botの名前
    print(discord.__version__)  # discord.pyのバージョン
    print('------')

client.run('TOKEN')
