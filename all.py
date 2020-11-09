import pprint

path = 'C:\\Users\\kiryu\\Desktop\\tuji\\textdata\\nucc\\'

def DataText(path):
    result_list = []
    with open(path+'data004.txt',"r",encoding="utf-8") as f:
        l = f.readlines()
    return l

def AttoMarkDelete(data):
    result = [i for i in data if i[0] != '＠']
    return result

if __name__ == "__main__":
    data = DataText(path)
    pprint.pprint(len(data))
    print(len(AttoMarkDelete(data)))
    