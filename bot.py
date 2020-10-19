import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='m.')

@bot.event
async def on_ready():
    print("Bot is ready")

@bot.event
async def on_message(message):
    # print('Message from {0.author}: {0.content}'.format(message))
    await bot.process_commands(message)

# @bot.event
# async def on_member_join(member):
#     print(f'{member} has joined a server')

# @bot.event
# async def on_member_remove(member):
#         print(f'{member} has left the server')

@bot.command()
async def ping(context):
    await context.send(f'Pong! {round(bot.latency * 1000)}ms')

@bot.command()
async def kick(context, member:discord.Member,*, reason=None):
    await member.kick(reason=reason)
    await context.send(f'```Kicked {member} from the server!\nReason for Kick: {reason}```')

@bot.command()
async def ban(context, member:discord.Member,*, reason=None):
    await member.ban(reason=reason)
    await context.send(f'```Banned {member} from the server!\nReason for Ban: {reason}```')

@bot.command()
async def clear(context, amount= 5):
    await context.channel.purge(limit=amount+1)
    await context.send(f'```Cleared {amount} Messages!```')

@bot.command(aliases=['8ball'])
async def _8ball(context, *, question):

    responses = [

        'As I see it, yes.',
        'Ask again later.',
        'Better not tell you now.',
        'Cannot predict now.',
        'Concentrate and ask again.',
        'Don’t count on it.',
        'It is certain.',
        'It is decidedly so.',
        'Most likely.',
        'My reply is no.',
        'My sources say no.',
        'Outlook not so good.',
        'Outlook good.',
        'Reply hazy, try again.',
        'Signs point to yes.',
        'Very doubtful.',
        'Without a doubt.',
        'Yes.',
        'Yes – definitely.',
        'You may rely on it.'
    ]

    await context.send(f'Question : {question}\nAnswer : {random.choices(responses)[0]} ')



bot.run('NzY3NjE0NzUzOTI4NjQyNTgw.X40e8g.R9y7c4HPXEZy8Sc-5uGhKjoiN2U')




# import discord

# class Mybot(discord.bot):
#     async def on_ready(self):
#         print('Logged on as {0}!'.format(self.user))

#     async def on_message(self, message):
#         print('Message from {0.author}: {0.content}'.format(message))

#     async def on_member_join(self,member):
#         print(f'{member} has joined a server')

#     async def on_member_remove(self,member):
#         print(f'{member} has left the server')

# bot = Mybot()
# bot.run('NzY3NjE0NzUzOTI4NjQyNTgw.X40e8g.R9y7c4HPXEZy8Sc-5uGhKjoiN2U')