from PIL import Image, ImageColor, ImageDraw
import random
import json
import math

with open('order-5.json') as f:
  data = json.load(f)

for ti, d in enumerate(data):
  main = int(d["card"])
  tmp = d["list"].split(",")
  edges = list(map(int, tmp))
  edges.remove(main) #remove MAIN from within
  random.shuffle(edges)

  pngmain = "pictures/image-" + str(main).zfill(2) + ".png"
  pngedge = []
  for e in edges:
    pngfile = "pictures/image-" + str(e).zfill(2) + ".png"
    pngedge.append(pngfile)

  imgMain = Image.open(pngmain)
  imgEdge = [Image.open(x) for x in pngedge]

  card = Image.new('RGBA', (1000, 1000), (255, 0, 0, 0))

  twitch = ti * 3.1415 / 7
  for i in range(0,5):
    im = imgEdge[0].resize((150,150))
    ang = twitch + (i * ((2 * 3.1415) / 5))
    x = math.floor(380 * math.cos(ang)) 
    y = math.floor(380 * math.sin(ang)) 
    im = imgEdge[i].resize((150,150))
    card.paste(im, (500-75-x,500-75-y), im)

  im = imgMain.resize((400,400))
  card.paste(im, (500-200,500-200), im)

  draw = ImageDraw.Draw(card)
  draw.ellipse((5, 5, 995, 995), outline ='black', width=10)

  card.save("cards5/card-" + str(main).zfill(2) +".png")