import math
from PIL import Image, ImageColor, ImageDraw, ImagePath, ImageFilter
import random
import json
import math
import sys

def main(val):
  side = 8
  xy = [
      (math.ceil((math.cos(th) + 1) * 530 +220),
       math.ceil((math.sin(th) + 1) * 530 -30))
      for th in [(i * (2 * math.pi) / side) + (math.pi/8)  for i in range(side+1)]
      ]  
      
  with open('order-7.json') as f:
    data = json.load(f)

  for ti, d in enumerate(data):
    main = int(d["card"])
    if (val != -1) and (val != main):
      #print(val,main)
      continue
    print(main)
    tmp = d["list"].split(",")
    edges = list(map(int, tmp))
    if main not in edges:
      print("Error: main not in edges")
      exit(1)
    edges.remove(main) #remove MAIN from within
    random.shuffle(edges)

    pngmain = "pictures/image-" + str(main).zfill(2) + ".png"
    pngedge = []
    for e in edges:
      pngfile = "pictures/image-" + str(e).zfill(2) + ".png"
      pngedge.append(pngfile)

    imgMain = Image.open(pngmain)
    #imgMain = imgMain.filter(ImageFilter.GaussianBlur(radius=4))
    imgEdge = [Image.open(x) for x in pngedge]

    card = Image.new('RGBA', (1500, 1000), (255, 255, 255, 255))

    for i in range(0,7):
      im = imgEdge[0].resize((200,200))
      ang = (i * ((2 * 3.1415) / 7)) + (3.1415/2)
      x = math.floor(360 * math.cos(ang)) 
      y = math.floor(360 * math.sin(ang)) 
      im = imgEdge[i].resize((180,180))
      card.paste(im, (750-90-x,500-90-y), im)

    im = imgMain.resize((400,400))
    card.paste(im, (750-200,500-200), im)

    draw = ImageDraw.Draw(card)
    draw.line(xy, fill="black", width=10)

    card.save("cards7/card-" + str(main).zfill(2) +".png")

if __name__ == '__main__':
  try:
    cnt = len(sys.argv) - 1
    if cnt == 1:
        main(int(sys.argv[1]))
    else:
      main(-1)
  except IndexError:
    main(-1)
  
  
