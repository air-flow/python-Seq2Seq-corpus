import MeCab
import pprint
import re
path = 'C:\\Users\\kiryu\\Desktop\\tuji\\textdata\\nucc\\'
file = path+'data001.txt'
def DataText(path):
    result_list = []
    with open(file,"r",encoding="utf-8") as f:
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

def MeCabWakatigaki(text):
    m = MeCab.Tagger("-Owakati")
    # return m.parse(text).rstrip("\n")
    return m.parse(text)


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

def WriteTextInFile(data):
    mecab_data = list(map(MeCabWakatigaki,data))
    # even,odd = AlternateListChange(mecab_data)
    # output_list = ["input","output"]
    # すべての文が発話文であり、かつ応答文であると解釈する
    input_text = mecab_data[0:-1]
    output_text = mecab_data[1:]
    with open(path+"..//seq2seqtext\\input\\input.txt", mode='w',encoding='utf-8') as f:
        f.writelines(input_text)
    with open(path+"..//seq2seqtext\\output\\output.txt", mode='w',encoding='utf-8') as f:
        f.writelines(output_text)
    print("SUCCESS")
def AlternateListChange(data):
    even = data[0::2]
    odd = data[1::2]
    return even,odd

if __name__ == "__main__":
    data = DataText(path)
    # pprint.pprint(ldata))
    user_text = AttoMarkDelete(data)
    # pprint.pprint(AttoMarkDelete(data))
    # pprint.pprint(UnionText(user_text))
    temp =UnionText(user_text)
    WriteTextInFile(temp)