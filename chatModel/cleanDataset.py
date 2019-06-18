#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyarabic.araby as araby
import pyarabic.number as number

import re
i=0
emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)

outerTable='0123456789\'".abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRS)TUVWXYZ/@ᖇᗩᗰᗩᗪᗩᑎнυєɪиαв_=#>&%:،'
remove_char= '!(*+-;<?[\\]^`{|}~¡£¤¥§©«®°¶»¿ÀÁÃÄÅÊÎÑÓÖ×Üßàáâãäåçèéêëïñôõö÷øýÿāăĄĆćďĐĘĚěğĠĢĥĦĩķĺľŁłŃňŒŕŘřśŝŞşŠšţūŷżƏǮǻǿȜəɞʚ̨̐ΠΣπσϊмѕ؛؟٪ٰےۓ۔ۖۙۚ۞ۦ۩۱۽ღᴥᵔṚắếớ\u200f–—‘’“”„•…‰⁉\u2066\u2069₩€⃣℅ℓ™←∆√⊙⏬⏰Ⓜ▒▓■□▪●☀☁★☆☕☘☝☠☪☹☺☻♀♂♋♛♠♡♣♥♧⚓⚘⚠⚡⚪⚽⛅⛑⛔✅✈✉✊✋✌✍✔✝✞✡✨✿❄❇❌❓❔❕❗❣❤➖➡➰➿⬅⬆⬛⭐⭕《》ツ㊙彡\ue022\ue106\uf04a\uf8ff﴾﴿ﷺﷻ﷽🤔'

maxQues=0
maxAns=0
Questions=[]
Answers=[]
data_path = 'chatModel/data/cleanFile.txt'
file = open(data_path,'r',encoding="utf_8")
test = file.readlines()
file.close()
newFile=open('cleanFile.txt','w',encoding="utf_8")
for line in test:
    remove_digits = str.maketrans('','',remove_char)
    #res=emoji_pattern.sub(r'', line)
    line = line.translate(remove_digits)
    #res=araby.strip_tashkeel(res)
    #res=araby.strip_tatweel(res)
    #res=araby.normalize_hamza(res)
    #res=araby.normalize_ligature(res)
    #hasQuesAns=res.split(',')
    #if len(hasQuesAns) > 1:
    #    QuesText=""
    #    for i in range(len(hasQuesAns)):
    #        if i>0:
    #            QuesText+=" "+hasQuesAns[i]
    #    if len(hasQuesAns[0]) <1500 and len(QuesText)<1500 and len(hasQuesAns[0]) >3 and len(QuesText)>3 :
    #        Answers.append(hasQuesAns[0])
    #        Questions.append(QuesText)
    #        ln=u''+hasQuesAns[0]+"$splt$"+QuesText
    newFile.write(line)
newFile.close()

