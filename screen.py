import pprint
import codecs
import glob
import io
def GetFileContens(file_name):
    l = None
    with open(file_name,encoding='utf-8',mode='r') as target:
        l = target.readlines()
        l = list(map(lambda x: x.replace( '\n' , '' ),l))
    return l

def SetFileContens(l,file_name="temp"):
    puts = ["input","output"]
    input_data = l[:-1:2]
    output_data = l[1::2]
    set_data = dict(zip(puts,[input_data,output_data]))
    for types,data in set_data.items():
        path = "/".join(['.','mine','data',"scenario",types,file_name.split("\\")[-1]])
        with open(path,encoding='utf-8',mode='w') as target:
            target.writelines(list(map(lambda x: str(x)+"\n",data)))

def DeleteParentheses(text):
    if "」" in text:
        i = text.find("「")+1
        j = text.index("」")
        return text[i:j]
    else:
        return False

def DeleteSpace(text):
    return text.split()[-1]
def EncodeFile():
    file_list = FileList()
    for i in file_list:
        try:
            temp = i.split("\\")
            shiftjis_csv_path = i
            utf8_csv_path = './mine/scenario/utf/'+temp[-1]
            fin = codecs.open(shiftjis_csv_path, "r",'cp932')
            fout_utf = codecs.open(utf8_csv_path, "w", "utf-8")
            for row in fin:
                fout_utf.write(row)
            fin.close()
            fout_utf.close()
        except Exception as identifier:
            print(identifier,shiftjis_csv_path)
def main(file_name):
    file = GetFileContens(file_name)
    text_list =[i for i in list(map(DeleteSpace,file)) if i != False]
    # pprint.pprint(text_list)
    SetFileContens(text_list,file_name)

def FileList():
    files = glob.glob("./mine/scenario/utf/*")
    result = []
    for file in files:
        if "txt" in file:
            result.append(file)
            # print(file)
    return result


if __name__ == "__main__":
    # FileList()
    # EncodeFile()
    file_list = FileList()
    for i in file_list:
        if "2734" in i:
            main(i)
    pass