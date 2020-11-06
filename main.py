import pprint
import re
from typing import Match
import copy
import MeCab
def FileRead(i):
    file_name = path + "data" + i.zfill(3) + ".txt"
    with open(file_name ,"r", encoding="utf-8") as f:
        l = f.readlines()
        l =  [text for text in l if text.find('＠参加者') != -1 ]
        print(l)

def main():
    for i in range(1,130,1):
        FileRead(str(i))

def DataTextMember(path):
    result_list = []
    with open(path,"r",encoding="utf-8") as f:
        l = f.readlines()
        # print(MembersList(l))
        result_list.append(MembersList(l))
    return result_list

def DataText(path):
    result_list = []
    with open(path,"r",encoding="utf-8") as f:
        l = f.readlines()
    return l


def MembersList(parameter_list):
    member_list ={}
    l =  [text.rstrip('\n') for text in parameter_list if text.find('＠参加者') != -1 ]
    for i in l:
        index = i.find("＠参加者")+len("＠参加者")
        rust_index = i.find("：")
        key = i[index:rust_index]
        value = i[rust_index+1:]
        if MatchMember(key):
            member_list[key] = value
    return member_list

def MatchMember(parameter_list):
    m = re.match(r'[a-zA-Z]+[0-9]+', parameter_list)
    if m != None:
        return True
    return False

def TapeExchange(parameter_list):
    if parameter_list != '＜テープ反転＞':
        return True
    return False

def MemberSpeechText(member_list):
    l = DataText(path)
    None_List = []
    for index in member_list:
        None_List.append(copy.deepcopy([]))
    result_list = dict(zip(member_list,None_List))
    speech_now = ''
    index = 0
    # pprint.pprint(l)
    while index < len(l):
        if MatchMember(l[index]):
            speech_now = CheckMembers(l[index])
            temp_text = ""
            while index < len(l)-1:
                temp_text += l[index].rstrip("\n")
                # print(temp_text,index)
                index+=1
                if MatchMember(l[index]) and CheckMembers(l[index]) != speech_now :
                    result_list[speech_now].append(temp_text)
                    break
            else:
                result_list[speech_now].append(l[index-1].rstrip("\n"))
        else:
            index+=1
    return result_list

def CheckMembers(text):
    try:
        m = re.match(r'[a-zA-Z]+[0-9]+', text)
        return m.group()
    except Exception as identifier:
        return False

def SplitArticle(data):
    result = []
    r = data[list(data.keys())[0]]
    l = data[list(data.keys())[1]]
    # pprint.pprint(l)
    # print(len(r),len(l))
    # print(r)
    for i in range(0,len(r),1):
        # print(MeCabWakatigaki(i[i.find("：")+1:]))
        # print(i[l[i].find("：")+1:])
        print(l[i][:10],r[i][:10])
    #     pass

def MeCabWakatigaki(text):
    m = MeCab.Tagger("-Owakati")
    return m.parse(text)

if __name__ == "__main__":
    path = 'C:\\Users\\kiryu\\Desktop\\tuji\\textdata\\nucc\\data124.txt'
    l = DataText(path)
    member_list = MembersList(l).keys()
    result = MemberSpeechText(member_list)
    # print(list(member_list))
    # pprint.pprint(result)
    SplitArticle(result)
    # print(len(result[list(member_list)[0]]))
    # print(len(result[list(member_list)[1]]))
    # m = MeCab.Tagger("-Owakati")
    # print(m.parse("平服でお越しくださいと記載されている場合は、普段着でいくようにしている。"))
