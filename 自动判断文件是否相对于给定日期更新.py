from 切换工作目录 import browse_directory

import os
from datetime import datetime

def 自动判断文件是否相对于给定日期更新(after_that_time="2025-01-19 10:30:14"):
    browse_directory("❓需要判断是否相对于给定日期更新的所有文件在哪个目录下？(会自动查看所选目录下的全部子目录下的文件)",os.getcwd())
    
    new_only=False
    fmt="%Y-%m-%d %H:%M:%S"
    while True:
        answer=input("❓用于比较是否在这之后修改的给定日期是(日期格式:年-月-日 时:分:秒)：\n(Enter:默认)\n")
        if not answer:
            if not isinstance(after_that_time, (datetime, str)):
                print("❌默认日期必须是datetime类型对象或str类型对象\n")
                continue
            if isinstance(after_that_time, datetime):
                try:after_that_time_formated = datetime.strptime(after_that_time.strftime(fmt),fmt)
                except:
                    print(f"❌默认日期格式不对: {after_that_time.__repr__()}")
                    continue
            elif isinstance(after_that_time, str):                     
                try:after_that_time_formated=datetime.strptime(after_that_time,fmt)
                except:
                    print(f"❌默认日期格式不正确: {after_that_time.__repr__()}")
                    continue
            break
        try:after_that_time_formated=datetime.strptime(answer, fmt)
        except Exception as e:
            print("❌日期格式不正确")
            print(type(e).__name__,e,sep=":",end="\n"*2)
            continue
        break
    print("⚡️你的决定：给定日期是:\n",after_that_time_formated,end="\n"*2,sep="")
    after_that_time=str(after_that_time_formated)
    content=f"⚡️给定日期：{after_that_time_formated}（将修改日期与之对比是否在这之后，从而获知哪些文件是更新了的，从而避免漏把更新了的文件及时上传）\n"
   
    if input("❓是否仅展示更新的文件？\n(Enter:否(默认)|Y/y:是)\n").lower()=="y":
        new_only=True
    print("⚡️你的决定：仅展示更新的文件:", "是" if new_only else "否",end="\n"*2)
        
    roots_size=0
    for root,dirs,files in os.walk(os.getcwd()):       
        root_size=0
        # 排除目录名
        # 包括将远程仓库克隆到本地而产生的.git隐藏目录
        if [ True for _ in ("实验证明","版本跟进说明", ".git") if _ in root]:continue
        content+=f"\n⚡️--- Next Root ---\n{root}\n"
        files.sort(key=lambda x:(os.path.getmtime(os.path.join(root,x)),os.path.getsize(os.path.join(root,x))),reverse=True)
        for f in files:
            # 是否取消隐藏文件
            #if f.startswith("."):continue            
            is_new=False
            time_formated=datetime.fromtimestamp(os.path.getmtime(os.path.join(root,f)))
            if time_formated>after_that_time_formated:
                is_new=True
            # 展示全部文件 或 仅展示更新的文件
            # 如果new_only开启，则文件必须是新的才展示，否则跳过这个文件，到下一个文件
            if (not new_only) or (new_only and is_new):
                content+=f"{f}\n修改时间:{time_formated}"
                if is_new:content+="(更新了)\n"
                else:content+="\n"
                file_size=os.path.getsize(os.path.join(root,f))
                content+=f"文件大小: {file_size} 字节\n\n"
            root_size+=file_size
        content+=f"目录大小: {root_size} 字节\n"
        roots_size+=root_size
    content+=f"\n全部内容总大小: {roots_size} 字节\n"
    
    named="modify_time"    
    answer=input("❓请起名给用于保存这些信息的一个文件：\n(Enter:使用默认名称)\n")
    if answer:named=answer
    if new_only:named+="_new_only"
    named+=".txt"
    browse_directory(f"❓将生成的{named}保存在哪个目录",os.getcwd())
    
    with open(named,"w",encoding="utf-8") as f:
        f.write(content)
            
    print(f"✅所有文件的修改时间及大小已保存完毕！")
    
    return after_that_time

def main():
    os.chdir(os.path.dirname(__file__))
    default_setting_after_that_time=datetime.now()
    while True:
        default_setting_after_that_time=自动判断文件是否相对于给定日期更新(default_setting_after_that_time)
        input("按任意键继续...\n")

if __name__=="__main__":main()

