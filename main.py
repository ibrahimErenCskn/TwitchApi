from twitchio.ext import commands
import requests
import random
import json
class Bot(commands.Bot):
    def __init__(self):
        self.arr = []
        self.jsonVeri = {}
        self.giveawey_run = False
        self.winner = []
        self.time = 0
        self.url = "http://127.0.0.1:5000/katilimcilarPost"
        super().__init__(token='vvfvj5fbvy0d3huifxummnh78i4pac', prefix='!', initial_channels=['Erencskn51'])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    @commands.command()
    async def katil(self, ctx: commands.Context):
        if self.giveawey_run:
            if ctx.author.name in self.arr:
                await ctx.send("Sen Zaten Çekilişe Katıldın! "+ctx.author.name)
            else:
                self.arr.append(ctx.author.name)
            print(self.arr)
        else:
            await ctx.send("Herhangi Bir Çekiliş Başlatılmadı.")

    @commands.command()
    async def cekilisbaslat(self, ctx: commands.Context, *args):
        if ctx.author.is_mod:
            self.giveawey_run = True
            await ctx.send("Çekiliş Başlatıldı !katil ile Katılabilirsiniz.")

    @commands.command()
    async def cekilisbitir(self, ctx: commands.Context):
        if ctx.author.is_mod:
            self.giveawey_run = False
            if self.arr:
                self.jsonVeri ={
                    "Katilimcilar": self.arr
                }
                requests.post(self.url, json=self.jsonVeri)
                self.jsonVeri = {}
                await ctx.send(f"Çekiliş Bitirilmiştir Kazanan: {random.choice(self.arr)}")
            self.arr = []


bot = Bot()
bot.run()