import discord
import tmdbsimple as tmdb

TRENDING_MEDIA_TYPE = 'movie'
TRENDING_TIME_WINDOW = 'week'
media_type = TRENDING_MEDIA_TYPE
time_window = TRENDING_TIME_WINDOW

TRENDING1_MEDIA_TYPE = 'tv'
TRENDING1_TIME_WINDOW = 'week'
media1_type = TRENDING1_MEDIA_TYPE
time1_window = TRENDING1_TIME_WINDOW

trend = tmdb.Trending('movie', 'week')
trend1 = tmdb.Trending('tv', 'week')
trend.info()
trend1.info()
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!tmovie'):
        for c in trend.results:
            embed = discord.Embed(title=c['title'], colour=discord.Colour(0x331b17), url="https://www.themoviedb.org/movie/" + str(c['id']), description=c['overview'])

            embed.set_image(url="https://image.tmdb.org/t/p/original"+c['poster_path'])
            embed.set_thumbnail(url="https://www.themoviedb.org/assets/2/v4/logos/v2/blue_square_2-d537fb228cf3ded904ef09b136fe3fec72548ebc1fea3fbbd1ad9e36364db38b.svg")

            embed.add_field(name="ratings", value=c['vote_average'])
            embed.add_field(name="Release Date", value=c['release_date'])
            embed.add_field(name="original language", value=c['original_language'])
            await message.channel.send(embed=embed)
    if message.content.startswith('!ttv'):
        for c in trend1.results:
            embed = discord.Embed(title=c['name'], colour=discord.Colour(0x331b17), url="https://www.themoviedb.org/tv/" + str(c['id']), description=c['overview'])

            embed.set_image(url="https://image.tmdb.org/t/p/original"+c['poster_path'])
            embed.set_thumbnail(url="https://www.themoviedb.org/assets/2/v4/logos/v2/blue_square_2-d537fb228cf3ded904ef09b136fe3fec72548ebc1fea3fbbd1ad9e36364db38b.svg")

            embed.add_field(name="ratings", value=c['vote_average'])
            embed.add_field(name="First air date", value=c['first_air_date'])
            embed.add_field(name="original language", value=c['original_language'])
            await message.channel.send(embed=embed)

client.run(clientid)
