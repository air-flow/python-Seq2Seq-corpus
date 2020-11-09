import pprint
import re
path = 'C:\\Users\\kiryu\\Desktop\\tuji\\textdata\\nucc\\'

def DataText(path):
    result_list = []
    with open(path+'data004.txt',"r",encoding="utf-8") as f:
        l = f.readlines()
    return l

def AttoMarkDelete(data):
    result = [i for i in data if i[0] != '＠']
    return result


def MatchMember(parameter_list):
    m = re.match(r'[a-zA-Z]+[0-9]+', parameter_list)
    if m != None:
        return True
    return False

def UnionText(data):
    index = 0
    result = []
    while index < len(data):
        temp = data[index].rstrip("\n")
        if MatchMember(temp):
            result.append(temp)
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