import discord
import pytz
import datetime
import requests
from bs4 import BeautifulSoup

url = 'https://pnr2.patolesoft.net/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
jst = pytz.timezone('Asia/Tokyo')
date = datetime.datetime.now(jst)
weekday = date.weekday()
day = str(date.day)
month = str(date.month)
hour = str(date.hour)
mimu = str(date.minute)

async def get_myriad(ctx):
    
    if weekday == 0:
     embed=discord.Embed(title="今日のミリアド開催時刻は…", color=0xe8f906)
     embed.add_field(name="開催時刻", value=f"ミリアドJPゲーム: {month}/{day} - 20:00", inline=False)
     await ctx.send(embed=embed)
    elif weekday == 1:
     embed=discord.Embed(title="今日のミリアド開催時刻は…", color=0xe8f906)
     embed.add_field(name="開催時刻", value=f"ミリアドレース: {month}/{day} - 18:00〜18:25", inline=False)
     embed.add_field(name="対象ゲーム", value="パトルプッシャープレゼンス\nパトルプッシャーリアライズ\nトリプレットシャワー\nスカイドリーム\nスフィードパラダイス\nパスロット\nパトルーレット", inline=False)
     await ctx.send(embed=embed)
    elif weekday == 2:
     embed=discord.Embed(title="今日のミリアド開催時刻は…", color=0xe8f906)
     embed.add_field(name="開催時刻", value=f"ミリアドJPゲーム: {month}/{day} - 21:00", inline=False)
     await ctx.send(embed=embed)
    elif weekday == 3:
     embed=discord.Embed(title="今日のミリアド開催時刻は…", color=0xe8f906)
     embed.add_field(name="開催時刻", value=f"ミリアドレース: {month}/{day} - 20:00〜20:25", inline=False)
     embed.add_field(name="対象ゲーム", value="パトルプッシャープレゼンス\nパトルプッシャーリアライズ\nトリプレットシャワー\nスカイドリーム\nスフィードパラダイス\nブラックジャック\nフルーツチェイン", inline=False)
     await ctx.send(embed=embed)
    elif weekday == 4:
     embed=discord.Embed(title="今日のミリアド開催時刻は…", color=0xe8f906)
     embed.add_field(name="開催時刻", value=f"ミリアドJPゲーム: {month}/{day} - 22:00", inline=False)
    elif weekday == 5:
     embed=discord.Embed(title="今日のミリアド開催時刻は…", color=0xe8f906)
     embed.add_field(name="開催時刻", value=f"ミリアドJPゲーム: {month}/{day} - 20:00\nミリアドレース: {month}/{day} - 20:30〜20:55", inline=False)
     embed.add_field(name="対象ゲーム", value="パトルプッシャープレゼンス\nパトルプッシャーリアライズ\nトリプレットシャワー\nスカイドリーム\nスフィードパラダイス\nパスロット\nパトルーレット", inline=False)
     await ctx.send(embed=embed)
    elif weekday == 6:
     embed=discord.Embed(title="今日のミリアド開催時刻は…", color=0xe8f906)
     embed.add_field(name="開催時刻", value=f"ミリアドJPゲーム: {month}/{day} - 21:00\nミリアドレース: {month}/{day} - 21:30〜21:55", inline=False)
     embed.add_field(name="対象ゲーム", value="パトルプッシャープレゼンス\nパトルプッシャーリアライズ\nトリプレットシャワー\nスカイドリーム\nスフィードパラダイス\nブラックジャック\nフルーツチェイン", inline=False)
     await ctx.send(embed=embed)

async def get_event(ctx):
    target_div = soup.find('div', {'class': 'col-lg-12 pb-1 text-center'})
    img_tags = target_div.find_all('img')['src']
    target_div2 = soup.find('div', {'class': 'col-lg-12 pb-1 text-center'})
    img_tags2 = target_div.find_all('img')['src']
    embed1=discord.Embed(title="イベント情報その1", color=0x1eff00)
    embed1.set_image(url=img_tags)
    embed2=discord.Embed(title="イベント情報その2", color=0x1eff00)
    embed2.set_image(url=img_tags2)
    await ctx.send(embed=embed1)
    await ctx.send(embed=embed2)
