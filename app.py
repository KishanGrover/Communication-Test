import os
import logging
from flask import Flask, request, redirect, jsonify
import time
from datetime import datetime

app = Flask(__name__)
app.secret_key = "secret key"
@app.route('/', methods=['POST'])
def processjson():
    with open('tb.txt', 'a+') as f:
        try:
            data=request.get_json()
            para=data["inputstr"]
            mandatorys_word_list=data["mandatory"]
            a=word_count(para)
            b=words(para)
            c=unique_words(para,mandatorys_word_list)
            d=spell(para)
            e=grammar(para)
            f=sentence(para)


            #end=time.time()

            return jsonify({"wordCount":a,"vocabCount":b,"specialKeywords":c,"spellCheckCount":d,"grammarCount":e,"sentenceCount":f})
        except:
            
            # Getting Datetime from timetamp
            now=datetime.now()
            date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

            #print(date_time)
            f.write(date_time)
            import traceback
            traceback.print_exc(file=f)
    
    # code to process download her
def removenull(para):
    #new=para.replace(" ","")
    para=para.rstrip()
    para=para.lstrip()
    if len(para)==4:
        newsplit=para.split(" ")
        if len(newsplit)==1:
    #print(newsplit)
            for i in newsplit:
                if i=="Null" or i=="null":
                    newsplit=[]
            para=" ".join(newsplit)
    return para
    
    
def word_count(para):
    para=removenull(para)
    para=para.lstrip()
    para=para.rstrip()
    if len(para)==0 :
        res=0
        return res
    else:
        specialChars = "!#$%^&*()@:‘/.\><;|"
        for specialChar in specialChars:
            para = para.replace(specialChar, '')
            para=para.replace("  "," ")
        paragraph=para.split(" ")
        res=len(paragraph)
        return res
def words(para):
    para=removenull(para)
    common_words="""" the of to and a in is it you that he was for who they on know are with as I his they be at one have this from or had by not word but what some we can out other were all there when up use your how said an each she which do their time if will way about many then them write would like so these her long make thing see him two has look more day could go come did number sound  no most people my"""
    specialChars = "!#$%^&*(),:‘./\><;|"
    for specialChar in specialChars:
        para = para.replace(specialChar, '')
    set_common=set(common_words.split(' '))
    set_input=set(para.split(' '))
    set3=set_input-set_common
    res2=len(set3)
    return res2
def unique_words(para,mandatory_word_list):
    para=removenull(para)
    specialChars = "!#$%^&*(),:‘./\><;|"
    for specialChar in specialChars:
        para = para.replace(specialChar,'')
    set_str=set((para.lower()).split(" "))
    set_words=set((mandatory_word_list.lower()).split(" "))
    if len(set_words)==1:
        for i in set_words:
            if i=="":
                set_words={}
    res=set_str.intersection(set_words)
    return len(res)
def spell(para):
    para=removenull(para)
    para= para.lstrip()
    para=para.rstrip()
    if len(para)==0 or para==" " or para=="  ":
        corr=""
        return len(corr)
    else:
        from spellchecker import SpellChecker
        spell = SpellChecker(distance=1)
        para="".join(para)
        para=para.lower()
        specialChars = "!@#$%^&*(),:‘./\><;|"
        for specialChar in specialChars:
            para = para.replace(specialChar, '')
        text=para.split(" ")
        corr=[]
        for i in text:
            misspelled = spell.unknown([i])
            for word in misspelled:
                a=spell.correction(word)
                corr.append(para)
        return len(corr)
def grammar(para):
    para=removenull(para)
    if len(para)==0:
        count=0
        return count
    else:
        import language_tool_python
        tool = language_tool_python.LanguageToolPublicAPI('es')
        tool.disable_spellchecking()
        para="".join(para)
        text = para
        text=text.lower()
        texts=text.split(" ")
        abc=tool.correct(text)
        z=abc.lower()
        z=z.split(" ")
        count=0
        for i in texts:
            if i in z:
                count=count+0
            else:
                count=count+1
        return count

def sentence(para):
    para=removenull(para)
    para=para.lstrip()
    para=para.rstrip()
    if len(para)==0 :
        para=""
        return len(para)
    else:
        para="".join(para)
        c=para.split(".")
        res = []
        for ele in c:
            if ele.strip():
                res.append(ele)

        return len(res)

if __name__ == "__main__":
    app.run("0.0.0.0",port=5022, debug = True)
