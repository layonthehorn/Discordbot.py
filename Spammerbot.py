import discord, random, re

class MyClient(discord.Client):

    # This reports that the bot logged in from your console
    async def on_ready(self):
        print('Logged on as', self.user)
        await client.change_presence(activity=discord.Game(name='Cute Cat Videos!'))

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        else:



            await message.add_reaction("<:vernhappy:615357722870939709>")
            #print(message.author.name)
            #print(message.author.id)
            # Will post the avatar of who ever is posted in the comments
            if "!avatar" in message.content and message.mentions.__len__()>0:
                for user in message.mentions:
                    await message.channel.send(user.avatar_url)
            # Posts a random song
            if "!singsong" in message.content:
                listosongs = ["https://www.youtube.com/watch?v=ZyhrYis509A","https://www.youtube.com/watch?v=dtER80sOjX4","https://www.youtube.com/watch?v=LACbVhgtx9I","https://www.youtube.com/watch?v=E5VMZqgVzRo&list=FLY5xmikeJ50GVVgVDwNoEEA&index=15&t=0s","https://www.youtube.com/watch?v=eAmK6zPZQtc"]
                await message.channel.send(random.choice(listosongs))
            # posts the garbage day clip
            if "!garbageday" in message.content:
                await message.channel.send("Garbage Day!\nhttps://www.youtube.com/watch?v=i7gIpuIVE3k")
            # lists the commands for the bot
            if "!commands" in message.content:
                await message.channel.send("I can respond to the following:\n\n!credits - Prints credits\n\n!cute - cats please\n\n!lunchbox\n\n!avatar @username#### - To post the users avatar\n\n!singsong - To link a random youtube song.\n\n!source - Links the git page\n\n!garbageday - You'll find out\n\n!commands - This message.")
            # Responds to a post of lol
            if (re.search(r"(?i)\blol\b",message.content)):
                await message.channel.send("Don't say that junk here you fool!")
            # Reminds someone of their favorite book series!
            if message.content == "!lunchbox":
                await message.channel.send("lunchbox loves discworld bruh!")
            # Links the github page of this project
            if message.content == "!source":
                await message.channel.send("Source Code:\nhttps://github.com/layonthehorn/Discordbot.py/blob/master/Spammerbot.py")
            # States who created the bot... Me by the way
            if message.content == "!credits":
                await message.channel.send("This bot was made by @layonthehorn. Who is very cool, and attractive by the way.")
            if "!cute" in message.content:
                messagetosend = message.author.name
                await message.channel.send("{0} Loves cats!".format(messagetosend),tts=True)
                #await message.channel.send("Damn spammers!")
            if "!song" in message.content:
                listchan = discord.Client.get_all_channels(self)
                for i in listchan:
                    print(i)


client = MyClient()
client.run('TokenHere')

