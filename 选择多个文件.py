def select_multiple_files(从这些文件当中选择):
    print("⚡️将从以下文件中搜索:")
    for number, src_file in enumerate(从这些文件当中选择):
        print(number, ":", src_file, sep=str())
    
    mode=bool(input("❓模式切换(Enter:反选|任意:正选):\n"))

    while True:        
        if mode:answer=input("❓请选择需要进行搜索的文件(输入多个序号,以空格分隔)(Enter:搜索全部文件):\n")
        else:answer=input("❓请筛选掉不需要进行搜索的文件(输入多个序号,以空格分隔)(Enter:搜索全部文件):\n")
        
        if not answer:return 从这些文件当中选择
        answer=answer.split()
        
        try:answer=set([int(n) for n in answer])
        except:
            print("❌输入有误\n")
            continue
        if False in [0<=n<len(从这些文件当中选择) for n in answer]:
            print("❌序号不在可选范围内\n")
            continue
        break
    selected_files=[]
    [selected_files.append(src) for number,src in enumerate(从这些文件当中选择) if (number in answer) == mode]
    print("⚡️将从以下文件中搜索:")
    [print(_) for _ in selected_files]
    if not selected_files:print("❗️没有可搜索的文件！")
    return selected_files

def 生成一个用于测试的目录所有文件名(start_chr="a",numberOfFiles=10,suffix=".txt"):
    return ([ chr(_) + suffix for _ in range(ord(start_chr), ord(start_chr) + numberOfFiles) ])

def main():
    select_multiple_files(生成一个用于测试的目录所有文件名())
    
    
if __name__=="__main__":
    while True:
        main()
        input()    

# updated:2025.1.20
# 《选择多个文件》v1.0.0-beta

# updated:2025.12.24
# 在之前支持反选的基础上，支持正选。