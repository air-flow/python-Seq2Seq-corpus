import pprint

def GetFileContens(file_name):
    l = None
    with open('./mine/scenario/'+file_name,encoding='utf-8',mode='r') as target:
        l = target.readlines()
        l = list(map(lambda x: x.replace( '\n' , '' ),l))
    return l

def SetFileContens(l,file_name="temp"):
    puts = ["input","output"]
    input_data = l[:-1:2]
    output_data = l[1::2]
    set_data = dict(zip(puts,[input_data,output_data]))
    for types,data in set_data.items():
        path = "/".join(['.','mine','data',"scenario",types,file_name])
        with open(path,encoding='utf-8',mode='w') as target:
            target.writelines(list(map(lambda x: str(x)+"\n",data)))

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
    SetFileContens(text_list,file_name)
    # pprint.pprint(text_list)
    # pprint.pprint(list(map(DeleteParentheses,file)))
    # print(DeleteParentheses(file))
    # print(list([iter(range(2))]*1))
    # for i in expression_list:
    #     pass