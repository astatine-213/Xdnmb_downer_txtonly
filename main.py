from Xdnmb import Xdnmb
import os
# from Epub import Epub
# from Epub import TXT

if __name__=="__main__":
    if not os.path.exists("txtoutput"):
        os.mkdir("txtoutput")
    x = Xdnmb(r"PHPSESSID=*****; userhash=*****") #在这里输入你的PHPSESSID 和饼干userhash
    DID = 51340998      #在这里修改DID号码
    fin = x.get_all(DID)
    msg=""
    new_title=""#在这里加入文字信息来自定义标题,不需要后缀
    msg+=fin[0]["content"]
    for x in fin:
        for y in x['Replies']:
            msg+=y["content"]
            msg+="\n\n"
        msg+="\n"
    msg+=f"来自https://www.nmbxd1.com/t/{DID}\n版权归属原作者及X岛匿名版"

    if new_title=="":
        with open("txtoutput/"+fin[0]["title"]+".txt","w",encoding="utf-8") as f:
            f.write(msg.replace(r"<br />","").replace(r" ",""));f.close()
    else:
        with open("txtoutput/"+new_title+".txt","w",encoding="utf-8") as f:
            f.write(msg.replace(r"<br />","").replace(r" ",""));f.close()
