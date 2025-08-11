import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.ext import tasks
from discord.utils import get
import os
import kp
import telnetlib
from multiprocessing import Process
import mysql.connector
import time
import sqlite3
import random
import nest_asyncio

nest_asyncio.apply()
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
chat = []


async def getm(tn):
    sch = client.get_channel(889441697912745995)
    mes = sch.get_partial_message(890054158214897686)
    co = mysql.connector.connect(
        charset='utf8mb4',
        host='mysql-2c659f5d-koushik-0f01.d.aivencloud.com',
        user='avnadmin',
        password='AVNS_JdxE_ymdbe-j4srLh96',
        database='defaultdb')
    cu = co.cursor()
    cu.execute('SELECT msg FROM me')
    try:
        msg = cu.fetchall()[0][0]
        print(msg)
        co.close()
        if True:
            if len(chat) == 5:
                chat.remove(chat[0])
                if msg == chat[-1]:
                    pass
                else:
                    chat.append(msg)
            else:

                if chat != [] and msg == chat[-1]:
                    pass
                else:
                    chat.append(msg)
        tn.write("""
b=[]
for a in bsInternal._getGameRoster():
	try:
		b.append(a['players'][0]['nameFull'])
	except:
		b.append(a['displayString'])
print('|my|'.join(b))
""".encode('ascii') + b"\n")
        time.sleep(0.2)
        y = tn.read_very_eager().decode('utf8').replace('bombsquad>', '')
        y = y.split('|my|')
        y[-1] = y[-1].replace('\n ', '')
        st = "**---|Pixel|--- epic teams**"
        dev = "\n"
        dev1 = "ㅤㅤ"
        y = dev1.join(y)
        sd1 = "ㅤㅤㅤㅤ--------~< Online players >~-------            \n\n" + y
        sd = "\nㅤㅤㅤㅤㅤㅤㅤ-------~< Chat >~-------\n\n" + dev.join(
            chat) + dev + dev + sd1

        e = discord.Embed(title=st, description=sd, color=0x00ffff)
        await mes.edit(embed=e)
    except Exception as e:
        print(e)
    time.sleep(5)
    Process(target=await getm()).start()


@client.event
async def on_ready():
    global mydb
    global mycursor
    await client.change_presence(activity=discord.Streaming(
        name='"-help" ✨',
        url="https://youtube.com/channel/UCsdQ8M_98IfdCU1KP_Tgcmg"))
    print('logined as {0.user}'.format(client))
    import sqlite3
    mydb = sqlite3.connect('main.pix')
    mycursor = mydb.cursor()
    try:
        mycursor.execute(
            "CREATE TABLE serset(id VARCHAR(50), se VARCHAR(50), channel VARCHAR(50))"
        )
    except Exception as e:
        print(e)
    clear.start()


    #tn = telnetlib.Telnet(host="167.86.117.85",port='26290')
    #tn.read_until(b"password:")
    #tn.write("pixeltrue".encode('ascii') + b"\n")
    #Process(target=await getm(tn)).start()
@client.event
async def on_member_join(member):
    global mycursor
    sql = "SELECT * FROM serset WHERE id ='" + str(member.guild.id) + "'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        if x[1] == 'welmsg':
            cha = client.get_channel(int(x[2]))
            from PIL import Image, ImageFont, ImageDraw
            import requests
            im1 = Image.open(r"bg.jpg")
            im2 = Image.open(requests.get(member.avatar_url, stream=True).raw)
            im2 = im2.resize((300, 300))
            Image.Image.paste(im1, im2, (220, 100))
            title_font = ImageFont.truetype('CaviarDreams.ttf', 50)
            title_text = "Welcome to " + str(member.guild) + " server"
            image_editable = ImageDraw.Draw(im1)
            w, h = image_editable.textsize(title_text, font=title_font)
            if w > 740:
                title_font = ImageFont.truetype('CaviarDreams.ttf', 45)
                w, h = image_editable.textsize(title_text, font=title_font)
            if w > 740:
                title_font = ImageFont.truetype('CaviarDreams.ttf', 40)
                w, h = image_editable.textsize(title_text, font=title_font)
            if w > 740:
                title_font = ImageFont.truetype('CaviarDreams.ttf', 35)
                w, h = image_editable.textsize(title_text, font=title_font)
            image_editable.text(((740 - w) / 2, 0),
                                title_text, (255, 105, 180),
                                font=title_font)
            title_font = ImageFont.truetype('CaviarDreams.ttf', 25)
            title_text = str(member)
            w, h = image_editable.textsize(title_text, font=title_font)
            image_editable = ImageDraw.Draw(im1)
            image_editable.text(((740 - w) / 2, 60),
                                title_text, (255, 192, 203),
                                font=title_font)
            re = str(member.id) + ".png"
            im1.save(re)
            fie = open(re, "rb")
            fi = discord.File(fie)
            await cha.send(file=fi)
            os.remove(re)


@client.event
async def on_member_remove(member):
    global mycursor
    sql = "SELECT * FROM serset WHERE id ='" + str(member.guild.id) + "'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        if x[1] == 'levmsg':
            cha = client.get_channel(int(x[2]))
            from PIL import Image, ImageFont, ImageDraw
            import requests
            im1 = Image.open(r"bg.jpg")
            im2 = Image.open(requests.get(member.avatar_url, stream=True).raw)
            im2 = im2.resize((300, 300))
            Image.Image.paste(im1, im2, (220, 100))
            title_font = ImageFont.truetype('CaviarDreams.ttf', 50)
            title_text = str(member) + "(-_-) Left, We have " + str(
                member.guild.member_count) + " members"
            image_editable = ImageDraw.Draw(im1)
            w, h = image_editable.textsize(title_text, font=title_font)
            if w > 740:
                title_font = ImageFont.truetype('CaviarDreams.ttf', 45)
                w, h = image_editable.textsize(title_text, font=title_font)
            if w > 740:
                title_font = ImageFont.truetype('CaviarDreams.ttf', 40)
                w, h = image_editable.textsize(title_text, font=title_font)
            if w > 740:
                title_font = ImageFont.truetype('CaviarDreams.ttf', 35)
                w, h = image_editable.textsize(title_text, font=title_font)
            image_editable.text(((740 - w) / 2, 0),
                                title_text, (255, 105, 180),
                                font=title_font)

            re = str(member.id) + ".png"
            im1.save(re)
            fie = open(re, "rb")
            fi = discord.File(fie)
            await cha.send(file=fi)
            os.remove(re)


@tasks.loop(seconds=59)
async def clear():
    try:
        os.remove('temp level')
    except:
        pass


@client.event
async def admin_message(message, m, a):
    global mycursor
    global mydb
    if message.author.guild_permissions.administrator:
        if m == '-setwelmsg':
            await message.channel.trigger_typing()
            if a[0]:
                sql = "SELECT * FROM serset WHERE id ='" + str(
                    message.guild.id) + "'"
                mycursor.execute(sql)
                myresult = mycursor.fetchall()
                check = 0
                for x in myresult:
                    if x[1] == 'welmsg':
                        if x[2] == a[0]:
                            await message.channel.send(
                                "<a:x_:832238330237419530>Bruh, No need to change it"
                            )
                            check = 1
                if check == 0:
                    sql = "UPDATE serset SET channel = '" + str(
                        a[0]) + "' WHERE id = '" + str(
                            message.guild.id) + "' AND se = 'welmsg'"
                    mycursor.execute(sql)
                    mydb.commit()
                    if mycursor.rowcount == 0:
                        sql = "INSERT INTO serset (id, se, channel) VALUES (?, ?, ?)"
                        val = (str(message.guild.id), "welmsg", str(a[0]))
                        mycursor.execute(sql, val)
                        mydb.commit()
                        await message.channel.send(
                            "<a:tick:832227557452939294>Successfully set welcome message"
                        )
                    else:
                        await message.channel.send(
                            "<a:tick:832227557452939294>Changed successfully")
            else:
                await message.channel.send(
                    "<a:x_:832238330237419530>Invalid arguement usage:- -setwelmsg channel id"
                )
        elif m == '-setlevmsg':
            await message.channel.trigger_typing()
            if a[0]:
                sql = "SELECT * FROM serset WHERE id ='" + str(
                    message.guild.id) + "'"
                mycursor.execute(sql)
                myresult = mycursor.fetchall()
                check = 0
                for x in myresult:
                    if x[1] == 'levmsg':
                        if x[2] == a[0]:
                            await message.channel.send(
                                "<a:x_:832238330237419530>Bruh, No need to change it"
                            )
                            check = 1
                if check == 0:
                    sql = "UPDATE serset SET channel = '" + str(
                        a[0]) + "' WHERE id = '" + str(
                            message.guild.id) + "' AND se = 'levmsg'"
                    mycursor.execute(sql)
                    mydb.commit()
                    if mycursor.rowcount == 0:
                        sql = "INSERT INTO serset (id, se, channel) VALUES (?, ?, ?)"
                        val = (str(message.guild.id), "levmsg", str(a[0]))
                        mycursor.execute(sql, val)
                        mydb.commit()
                        await message.channel.send(
                            "<a:tick:832227557452939294>Successfully set leave message"
                        )
                    else:
                        await message.channel.send(
                            "<a:tick:832227557452939294>Changed successfully")
            else:
                await message.channel.send(
                    "<a:x_:832238330237419530>Invalid arguement usage:- -setlevmsg channel id"
                )
        elif m == '-setsenart':
            await message.channel.trigger_typing()
            if a[0]:
                sql = "SELECT * FROM serset WHERE id ='" + str(
                    message.guild.id) + "'"
                mycursor.execute(sql)
                myresult = mycursor.fetchall()
                check = 0
                for x in myresult:
                    if x[1] == 'welmsg':
                        if x[2] == a[0]:
                            await message.channel.send(
                                "<a:x_:832238330237419530>Bruh, No need to change it"
                            )
                            check = 1
                if check == 0:
                    sql = "UPDATE serset SET channel = '" + str(
                        a[0]) + "' WHERE id = '" + str(
                            message.guild.id) + "' AND se = 'senart'"
                    mycursor.execute(sql)
                    mydb.commit()
                    if mycursor.rowcount == 0:
                        sql = "INSERT INTO serset (id, se, channel) VALUES (?, ?, ?)"
                        val = (str(message.guild.id), "senart", str(a[0]))
                        mycursor.execute(sql, val)
                        mydb.commit()
                        await message.channel.send(
                            "<a:tick:832227557452939294>Successfully set, you can now send beautiful arts 🎨"
                        )
                    else:
                        await message.channel.send(
                            "<a:tick:832227557452939294>Changed successfully")
            else:
                await message.channel.send(
                    "<a:x_:832238330237419530>Invalid arguement usage:- -setsenart channel id"
                )
        elif m == '-sem':
            pc = client.get_channel(878107683947954176)
            e = discord.Embed(title='---|pixel|--- epic ' + a[0],
                              description='ip:- ' + a[1] + '\nport:- ' + a[2],
                              color=0xFF69B4)
            e.set_thumbnail(url=a[3])
            await pc.send(embed=e)
        elif m == '-setlevel':
            await message.channel.trigger_typing()
            if a[0]:
                sql = "SELECT * FROM serset WHERE id ='" + str(
                    message.guild.id) + "'"
                mycursor.execute(sql)
                myresult = mycursor.fetchall()
                check = 0
                for x in myresult:
                    if x[1] == 'level':
                        if x[2] == a[0]:
                            await message.channel.send(
                                "<a:x_:832238330237419530>Bruh, No need to change it"
                            )
                            check = 1
                if check == 0:
                    sql = "UPDATE serset SET channel = '" + str(
                        a[0]) + "' WHERE id = '" + str(
                            message.guild.id) + "' AND se = 'level'"
                    mycursor.execute(sql)
                    mydb.commit()
                    if mycursor.rowcount == 0:
                        sql = "INSERT INTO serset (id, se, channel) VALUES ('" + str(
                            message.guild.id) + "', 'level', '" + str(
                                a[0]) + "')"
                        mycursor.execute(sql)
                        mydb.commit()
                        await message.channel.send(
                            "<a:tick:832227557452939294>Successfully set, now the level announcement send to it"
                        )
                    else:
                        await message.channel.send(
                            "<a:tick:832227557452939294>Changed successfully")
            else:
                await message.channel.send(
                    "<a:x_:832238330237419530>Invalid arguement usage:- -setlevel channel id"
                )
    else:
        pass


@client.event
async def on_message(message):
    global mycursor
    m = message.content.split(' ')[0]
    a = message.content.split(' ')[1:]
    if message.author == client.user:
        return
    elif m == '-help':
        await message.channel.trigger_typing()
        t1 = "Available commands"
        d1 = "```-sendart image url``` send your beautiful arts by this command (ex -sa http://img.png).\n```-say somthing``` say's somthing.\n```-avatar (person id optional)``` use to get your profile pic or other profile pic.\n```-level``` to get your level.\n```-ping``` to get the ping, cpu usage and ram usage.\n```-invite``` to invite this bot"
        t2 = "Settings commands"
        d2 = "```-setwelmsg channel id``` use this command to set welcome message or to change welcome message channel(ex:- -setwelmsg 1234567890).\n```-setlevmsg channel id``` use this command to set leave message or to change leave message channel(ex:- -setlevmsg 1234567890).\n```-setlevel channel id``` use this to set level announcement to desired channel(ex:- -setlevel 1233232).\n```-setsenart channel id``` use this command to set art channel or change art channel(ex:- -setsenart 12344466)."
        e = discord.Embed(title=t1, description=d1, color=0x9acd32)
        e.add_field(name=t2, value=d2, inline=False)
        e.add_field(name='ㅤ',
                    value='[support bot server](https://discord.gg/ShHyBaB)',
                    inline=False)
        await message.channel.send(embed=e)

    elif m == '-say' or m == '?say':
        await message.channel.trigger_typing()
        try:
            await message.channel.send(' '.join(a))
        except:
            try:
                await message.channel.send(a[0])
            except:
                await message.channel.send('hi')
    elif m == '-level':
        await message.channel.trigger_typing()
        import sqlite3
        from PIL import Image, ImageDraw, ImageFont
        conne = sqlite3.connect("level")
        cur = conne.cursor()
        sql1 = "SELECT lev FROM level WHERE id ='" + str(
            message.author.id) + "' AND ser ='" + str(message.guild.id) + "'"
        cur.execute(sql1)
        resu = cur.fetchone()
        if not resu:
            await message.channel.send("iam a bit busssy")
        else:
            level = resu[0]
            sql1 = "SELECT xp FROM level WHERE id ='" + str(
                message.author.id) + "' AND ser ='" + str(
                    message.guild.id) + "'"
            cur.execute(sql1)
            resu1 = cur.fetchone()
            xp = resu1[0]
            a = {}
            cur.execute("SELECT lev FROM level WHERE ser ='" +
                        str(message.guild.id) + "'")
            myresult2 = cur.fetchall()
            cur.execute("SELECT xp FROM level WHERE  ser ='" +
                        str(message.guild.id) + "'")
            myresult3 = cur.fetchall()
            myresult1 = []
            for e, f in zip(myresult2, myresult3):
                tem = int(e[0])
                le = 0
                while -1 < tem:
                    le = le + 100 + (tem - 1) * 80
                    tem = tem - 1
                toxp = le + int(f[0])
                myresult1.append(str(toxp))
            cur.execute("SELECT id FROM level WHERE ser ='" +
                        str(message.guild.id) + "'")
            myresult = cur.fetchall()
            for c, b in zip(myresult1, myresult):
                a[b[0]] = int(c)
            import ast
            u = str(sorted(a.items(), key=lambda x: (x[1], x[0]),
                           reverse=True))
            o = u.replace('(', '')
            o = o.replace(')', '')
            o = o.replace(", ", ':')
            o = o.replace("':", "',")
            o = o.replace('[', '{')
            o = o.replace(']', '}')
            o = o.replace("',", "':")
            o = o.replace(":'", ",'")
            z = ast.literal_eval(o)
            w = str(z.keys())
            e2 = w.replace('dict_keys', '')
            e4 = e2.replace("(['", "")
            e1 = e4.replace("'])", '')
            f1 = e1.split("', '")
            rank = str(int(f1.index(str(message.author.id))) + 1)
            user = str(message.author)

            def neededxp(level):
                return 100 + level * 80

            font = ImageFont.truetype('CaviarDreams.ttf', 28)
            if int(message.author.id) == 741246248908095529:
                font = ImageFont.truetype('NEON LED Light 400.ttf', 28)
            import requests
            medium_font = ImageFont.truetype('CaviarDreams.ttf', 22)
            small_font = ImageFont.truetype('CaviarDreams.ttf', 16)
            profile_bytes = Image.open(
                requests.get(message.author.avatar_url, stream=True).raw)
            profile_bytes = profile_bytes.resize((130, 130))
            im = Image.new('RGBA', (400, 148), (44, 44, 44, 255))
            im_draw = ImageDraw.Draw(im)
            im_draw.text((154, 5), user, font=font, fill=(255, 255, 255, 255))
            needed_xp = str(neededxp(int(level)))
            xp_text = f'Level {level}'
            im_draw.text((154, 62),
                         xp_text,
                         font=small_font,
                         fill=(255, 255, 255, 255))
            xp_text = 'Rank ' + rank
            im_draw.text((154, 42),
                         xp_text,
                         font=small_font,
                         fill=(255, 255, 255, 255))
            xp_text = f'{xp}/{needed_xp}'
            im_draw.text((314, 62),
                         xp_text,
                         font=small_font,
                         fill=(255, 255, 255, 255))
            im_draw.rectangle((174, 95, 374, 125), fill=(64, 64, 64, 255))
            im_draw.rectangle((174, 95, 174 +
                               (int(int(xp) / int(needed_xp) * 100)) * 2, 125),
                              fill='#FFD700')
            im_draw.rectangle((0, 0, 148, 148), fill=(255, 255, 255, 255))
            im.paste(profile_bytes, (10, 10))
            rep = str(message.author.id) + 'rank.png'
            im.save(rep)
            fie = open(rep, "rb")
            fi = discord.File(fie)
            await message.channel.send(file=fi)
            os.remove(rep)
            conne.close()
    elif m == '-5463573':
        await message.channel.trigger_typing()

        await message.add_reaction(client.get_emoji(832227557452939294))
    elif m == '-ping':
        import psutil
        channel = message.channel
        t1 = time.perf_counter()
        await message.channel.trigger_typing()
        t2 = time.perf_counter()
        e = discord.Embed(
            title="Bot™ info",
            description="ping:- ```{}ms```".format(round(
                (t2 - t1) * 1000)) + "\nCPU usage:- ```" +
            str(round(100 - psutil.cpu_percent(4))) + "```\nRAM usage:- ```" +
            str(round(100 - psutil.virtual_memory()[2], 2)) + "```",
            color=0xffd700)
        await message.channel.send(embed=e)
    elif m == '-invite':
        await message.channel.trigger_typing()
        await message.channel.send(embed=discord.Embed(
            title='invite link:-',
            description=
            'https://discord.com/api/oauth2/authorize?client_id=817668871163084801&permissions=198720&redirect_uri=http%3A%2F%2Fpixelteams.tk&scope=bot',
            color=0x0000ff))
    elif m == '-weltest':
        await message.channel.trigger_typing()
        sql = "SELECT * FROM serset WHERE id ='" + str(message.guild.id) + "'"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for x in myresult:
            if x[1] == 'welmsg':
                cha = client.get_channel(int(x[2]))
                from PIL import Image, ImageFont, ImageDraw
                import requests
                im1 = Image.open(r"bg.jpg")
                im2 = Image.open(
                    requests.get(message.author.avatar_url, stream=True).raw)
                im2 = im2.resize((300, 300))
                Image.Image.paste(im1, im2, (220, 100))
                title_font = ImageFont.truetype('CaviarDreams.ttf', 50)
                title_text = "Welcome to " + str(message.guild) + " server"
                image_editable = ImageDraw.Draw(im1)
                w, h = image_editable.textsize(title_text, font=title_font)
                if w > 740:
                    title_font = ImageFont.truetype('CaviarDreams.ttf', 45)
                    w, h = image_editable.textsize(title_text, font=title_font)
                    if w > 740:
                        title_font = ImageFont.truetype('CaviarDreams.ttf', 40)
                        w, h = image_editable.textsize(title_text,
                                                       font=title_font)
                        if w > 740:
                            title_font = ImageFont.truetype(
                                'CaviarDreams.ttf', 35)
                            w, h = image_editable.textsize(title_text,
                                                           font=title_font)
                image_editable.text(((740 - w) / 2, 0),
                                    title_text, (255, 105, 180),
                                    font=title_font)
                title_font = ImageFont.truetype('CaviarDreams.ttf', 25)
                title_text = str(message.author)
                w, h = image_editable.textsize(title_text, font=title_font)
                image_editable = ImageDraw.Draw(im1)
                image_editable.text(((740 - w) / 2, 60),
                                    title_text, (255, 192, 203),
                                    font=title_font)
                re = str(message.author.id) + ".png"
                im1.save(re)
                fie = open(re, "rb")
                fi = discord.File(fie)
                await cha.send(file=fi)
                os.remove(re)
                await message.add_reaction(client.get_emoji(832227557452939294)
                                           )
    elif m == '-avatar':
        await message.channel.trigger_typing()
        try:
            ab = a[0]
            await message.channel.send(
                message.guild.get_member(int(ab)).avatar_url)
        except Exception as e:
            await message.channel.send(str(e))
    elif m == '-sendart' or m == '-sa' or m == '-Sendart' or m == '-Sa':
        await message.channel.trigger_typing()
        sql = "SELECT * FROM serset WHERE id ='" + str(message.guild.id) + "'"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for x in myresult:
            if x[1] == 'senart':
                e = discord.Embed(color=0x00ff00)
                userID = message.author
                e.set_image(url=a[0])
                e.set_footer(text="-art by " + str(userID))
                cha = client.get_channel(int(x[2]))
                msg = await cha.send(embed=e)
                emoji = '\N{THUMBS UP SIGN}'
                await msg.add_reaction(emoji)
                emoji = '\N{THUMBS DOWN SIGN}'
                await msg.add_reaction(emoji)
                await message.add_reaction(client.get_emoji(832227557452939294)
                                           )
    else:
        await admin_message(message, m, a)
    if m == 'good morning':
        await message.channel.send("good morning " + message.author.mention)
    if m == 'good evening':
        await message.channel.send("good evening " + message.author.mention)
    if m == 'good night':
        await message.channel.send("good night " + message.author.mention)
    for msg in message.content.split(' '):
        if msg == 'pixel':
            await message.channel.send("?")
        elif msg == 'why' or msg == '?' or msg == 'whey' or msg == 'idk' or msg == 'dont' or msg == "don't":
            e = '\N{THINKING FACE}'
            await message.add_reaction(e)
        elif msg == 'ok' or msg == 'k' or msg == 'nothing' or msg == 'np' or msg == 'nop' or msg == 'n' or msg == 'noth':
            e = [
                '\N{HEAVY CHECK MARK}', '\N{THUMBS UP SIGN}',
                '\N{WHITE HEAVY CHECK MARK}', '\N{BALLOT BOX WITH CHECK}'
            ]
            r = random.randint(0, 3)
            await message.add_reaction(e[r])
    if not message.author.bot:
        sql = "SELECT * FROM serset WHERE id ='" + str(message.guild.id) + "'"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for x in myresult:
            if x[1] == 'level':
                chan = int(x[2])
                import sqlite3
                c = sqlite3.connect("level")
                c1 = sqlite3.connect("temp level")
                main = c.cursor()
                temp = c1.cursor()

                def neededxp(level):
                    return 100 + level * 90

                try:
                    main.execute(
                        "CREATE TABLE level (ser VARCHAR(50), id VARCHAR(50), lev VARCHAR(50), xp VARCHAR(50))"
                    )
                except:
                    pass
                try:
                    temp.execute(
                        "CREATE TABLE level (ser VARCHAR(50), id VARCHAR(50), xp VARCHAR(50))"
                    )
                except:
                    pass
                xp = len(message.content.split(' ')) * 1
                if xp > 50:
                    xp = 50
                sql = "SELECT xp FROM level WHERE id ='" + str(
                    message.author.id) + "' AND ser ='" + str(
                        message.guild.id) + "'"
                sql1 = "SELECT lev FROM level WHERE id ='" + str(
                    message.author.id) + "' AND ser ='" + str(
                        message.guild.id) + "'"
                sql2 = "SELECT xp FROM level WHERE id = '" + str(
                    message.author.id) + "' AND ser ='" + str(
                        message.guild.id) + "'"
                main.execute(sql1)
                myresult2 = main.fetchone()
                temp.execute(sql)
                myresult1 = temp.fetchone()
                main.execute(sql2)
                myresult = main.fetchone()
                if not myresult1:
                    sql = "INSERT INTO level (ser, id, xp) VALUES (?, ?, ?)"
                    val = (str(message.guild.id), str(message.author.id),
                           str(xp))
                    temp.execute(sql, val)
                    c1.commit()
                else:
                    if int(myresult1[0]) + xp >= 150:
                        sql = "UPDATE level SET xp = '150' WHERE id = '" + str(
                            message.author.id) + "' AND ser ='" + str(
                                message.guild.id) + "'"
                        temp.execute(sql)
                        c1.commit()
                        xp = 150 - int(myresult1[0])
                    else:
                        sql = "UPDATE level SET xp = '" + str(
                            int(myresult1[0]) + xp) + "' WHERE id = '" + str(
                                message.author.id) + "' AND ser ='" + str(
                                    message.guild.id) + "'"
                        temp.execute(sql)
                        c1.commit()
                xp = len(message.content.split(' ')) * 5
                if xp > 50:
                    xp = 50
                if not myresult:
                    sql = "INSERT INTO level (ser, id, lev, xp) VALUES (?, ?, ?, ?)"
                    val = (str(message.guild.id), str(message.author.id), "0",
                           str(xp))
                    main.execute(sql, val)
                    c.commit()
                else:
                    chan = chan
                    if not myresult1:
                        myresult1 = [0]
                    if int(myresult1[0]) + xp >= 150:
                        chan = chan
                        addxp = 150 - int(myresult1[0])
                        levch = neededxp(int(myresult2[0]))
                        if int(myresult[0]) + addxp == levch:
                            chan = chan
                            sql = "UPDATE level SET lev = '" + str(
                                int(myresult2[0]) +
                                1) + "' WHERE id = '" + str(
                                    message.author.id) + "' AND ser ='" + str(
                                        message.guild.id) + "'"
                            main.execute(sql)
                            c.commit()
                            sql = "UPDATE level SET xp = '0' WHERE id = '" + str(
                                message.author.id) + "' AND ser ='" + str(
                                    message.guild.id) + "'"
                            main.execute(sql)
                            c.commit()
                        elif int(myresult[0]) + addxp > levch:
                            put = int(myresult[0]) + addxp - levch
                            sql = "UPDATE level SET lev = '" + str(
                                int(myresult2[0]) +
                                1) + "' WHERE id = '" + str(
                                    message.author.id) + "' AND ser ='" + str(
                                        message.guild.id) + "'"
                            main.execute(sql)
                            c.commit()
                            sql = "UPDATE level SET xp = '" + str(
                                put) + "' WHERE id = '" + str(
                                    message.author.id) + "' AND ser ='" + str(
                                        message.guild.id) + "'"
                            chan = client.get_channel(chan)
                            main.execute(sql)
                            await chan.send("Ooya, " +
                                            str(message.author.mention) +
                                            " just advanced up level " +
                                            str(int(myresult2[0]) + 1) + "🎉.")
                            c.commit()
                        else:
                            sql = "UPDATE level SET xp = '" + str(
                                int(myresult[0]) +
                                addxp) + "' WHERE id = '" + str(
                                    message.author.id) + "' AND ser ='" + str(
                                        message.guild.id) + "'"
                            main.execute(sql)
                            c.commit()
                    else:
                        addxp = xp
                        levch = neededxp(int(myresult2[0]))
                        if int(myresult[0]) + addxp == levch:
                            sql = "UPDATE level SET lev = '" + str(
                                int(myresult2[0]) +
                                1) + "' WHERE id = '" + str(
                                    message.author.id) + "' AND ser ='" + str(
                                        message.guild.id) + "'"
                            chan = client.get_channel(chan)
                            await chan.send("Ooya, " +
                                            str(message.author.mention) +
                                            " just advanced up level " +
                                            str(int(myresult2[0]) + 1) + "🎉.")
                            main.execute(sql)
                            c.commit()
                            sql = "UPDATE level SET xp = '0' WHERE id = '" + str(
                                message.author.id) + "' AND ser ='" + str(
                                    message.guild.id) + "'"
                            main.execute(sql)
                            c.commit()
                        elif int(myresult[0]) + addxp > levch:
                            put = int(myresult[0]) + addxp - levch
                            sql = "UPDATE level SET lev = '" + str(
                                int(myresult2[0]) +
                                1) + "' WHERE id = '" + str(
                                    message.author.id) + "' AND ser ='" + str(
                                        message.guild.id) + "'"
                            chan = client.get_channel(chan)
                            await chan.send("Ooya, " +
                                            str(message.author.mention) +
                                            " just advanced up level " +
                                            str(int(myresult2[0]) + 1) + "🎉.")
                            main.execute(sql)
                            c.commit()
                            sql = "UPDATE level SET xp = '" + str(
                                put) + "' WHERE id = '" + str(
                                    message.author.id) + "' AND ser ='" + str(
                                        message.guild.id) + "'"
                            main.execute(sql)
                            c.commit()
                        else:
                            sql = "UPDATE level SET xp = '" + str(
                                int(myresult[0]) +
                                addxp) + "' WHERE id = '" + str(
                                    message.author.id) + "' AND ser ='" + str(
                                        message.guild.id) + "'"
                            main.execute(sql)
                            c.commit()
                c.close()
                c1.close()


kp.ke()
client.run('ODQxMjc2NTA3MDMyNzgwODAw.YJkZzQ.FKicyQ66PrGMAVZD7MICN9MtYEw')
