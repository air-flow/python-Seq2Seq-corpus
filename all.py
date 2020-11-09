import pprint
import re
path = 'C:\\Users\\kiryu\\Desktop\\tuji\\textdata\\nucc\\'

def DataText(path):
    result_list = []
    with open(path+'data005.txt',"r",encoding="utf-8") as f:
        l = f.readlines()
    return l

def AttoMarkDelete(data):
    result = [i for i in data if i[0] not in  ['＠','％']]
    return result


def MatchMember(parameter_list):
    m = re.match(r'[a-zA-Z]+[0-9]+', parameter_list)
    if m != None:
        return True
    return False

def BracketHittingEachOtherDeletion(text):
    return re.sub("[（）]", "", text)

def BracketMovementDeletion(text):
    return re.sub("[＜＞]", "", text)

def BracketFuriganaDeletion(text):
    return re.sub("[【】]", "", text)


def DeleteTextOpesion(text):
    # hitting_each_other （）delete （うん）（ふーん）
    # movement ＜＞ delete ＜録音中断＞ ＜笑い＞
    # furigana 【】 delete 【留学生の名前】
    # all movement and hitting_each_other and furigana delete
    hitting_each_other = BracketHittingEachOtherDeletion(text)
    movement = BracketMovementDeletion(text)
    furigana = BracketFuriganaDeletion(text)
    all =  BracketFuriganaDeletion(BracketMovementDeletion(hitting_each_other))
    return all

def NameDelete(text):
    index = text.find("：")
    return text[index+1:]

def UnionText(data):
    index = 0
    result = []
    while index < len(data):
        temp = DeleteTextOpesion(data[index].rstrip("\n"))
        if MatchMember(temp):
            name = NameDelete(temp)
            result.append(name)
        else:
            result[-1] = result[-1]+temp
        index+=1
    return result
if __name__ == "__main__":
    data = DataText(path)
    # pprint.pprint(ldata))
    user_text = AttoMarkDelete(data)
    # pprint.pprint(AttoMarkDelete(data))
    pprint.pprint(UnionText(user_text))