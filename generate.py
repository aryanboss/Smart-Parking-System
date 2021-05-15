import pandas as pd
from PIL import Image, ImageFont, ImageDraw

font = ImageFont.truetype("Roboto-Bold.ttf",size = 25)

def gentick(type,spot,tym,date,count):
    templet = Image.open("templet.png")
    k = str(count) + ".jpg"
    qr = Image.open(k).resize((325,325))#, Image.ANTIALIAS)
    x, y = qr.size
    templet.paste(qr,(0,0,x,y))
    draw = ImageDraw.Draw(templet)
    draw.text((510,95),str(type),font = font,fill='black')
    draw.text((510,155),str(spot),font = font,fill='black')
    draw.text((515,210),str(tym),font = font,fill='black')
    draw.text((440,263),str(date),font = font,fill='black')
    draw.text((240,330),str(count),font = font,fill='black')
    return templet


def make(type,spot,tym,date,count):
    tkt = gentick(type,spot,tym,date,count)
    ticket = "ticket"+str(count)+".png"
    tkt.save(ticket)