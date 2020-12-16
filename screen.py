import pprint

def GetFileContens(file_name):
    l = None
    with open('./mine/scenario/'+file_name,encoding='utf-8',mode='r') as target:
        l = target.readlines()
        l = list(map(lambda x: x.replace( '\n' , '' ),l))
    return l

def SetFileContens(l,file_name):
    l = None
    with open('./mine/data/scenario/input/'+file_name,encoding='utf-8',mode='x') as target:
        target.writelines(l)
        # l = list(map(lambda x: x.replace( '\n' , '' ),l))
    return l

def main():
    input/

def DeleteParentheses(text):
    if "」" in text:
        i = text.find("「")+1
        j = text.index("」")
        return text[i:j]
    else:
        return False
if __name__ == "__main__":
    file_name = "8uft8.txt"
    file = GetFileContens(file_name)
    text_list = list(map(DeleteParentheses,file))
    # pprint.pprint(text_list)
    # pprint.pprint(list(map(DeleteParentheses,file)))
    # print(DeleteParentheses(file))