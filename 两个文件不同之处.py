'''
import os,sys
sys.path.append(
	os.sep.join("/sdcard/[GuoYufan]/[Python]/文件管理/两个文件不同之处/".split("/"))
	)
from 两个文件不同之处 import 两个文件不同之处世界
cmp=toCompareTwoFile=两个文件不同之处世界()
del os,sys
'''


'''
import os,sys
here=__file__
#当设置为1 为回退到最底层目录
回退到上几级目录=3
for _ in range(回退到上几级目录):
    here=os.path.dirname(here)
del 回退到上几级目录, _


sys.path.append(
os.path.join(here, "你到哪里去/")
)
del os,sys
from 你到哪里去 import 你到哪里去世界
'''
	
from 切换工作目录 import *

# - import module

import os


class 两个文件不同之处世界():

# - variable defined
    
    def __init__(self,测试组名开头部分="测试组",测试组父目录=os.path.dirname(__file__)):
        self.测试组名开头部分=测试组名开头部分
        self.测试组父目录=测试组父目录
        self.chdir_at_startup=os.path.dirname(__file__)
        #self.你到哪里去 = 你到哪里去世界()  
        self.重置()
        
    def 重置(self):
        self.测试组合集=list()
        self.当前测试组=list()
        self.文件名1=self.文件名2=str()
        self.文件1=self.文件2=None
        self.less,self.more=self.内容1,self.内容2=(list(),list())
        self.不同之处带行号_more,self.不同之处带行号_less=([],[])      
        self.back = False
        
# - sub defined -
	
    def 获取测试组父目录(self):
        answer=input("❓你要去别处还是就在这里?\n"+\
"|去别处:T/t |退出:Q/q |否则在这里(以本文件所在目录或通过选项T/t最近os.chdir()到的目录的子目录为测试组)\n")
        if answer.lower()=="q":return "EXIT"
        if answer.lower()=="t":
            # 别初始化
            #self.你到哪里去.do()       
            self.chdir_at_startup=browse_directory(chdir_at_startup=self.chdir_at_startup)
            self.测试组父目录=os.getcwd()

    def 进入测试组父目录(self):
        os.chdir(self.测试组父目录)
        
    def 获取测试组名开头部分(self):
        print("现测试组名开头部分:",self.测试组名开头部分)
        answer=input("⚙️\n请设置(无需设置按Enter跳过):")
        if len(answer):self.测试组名开头部分=answer
        print()
    
    def 是目录吗(self,item):
        if not isinstance(item,str):
            raise TypeError("must be str, not "+type(item).__name__)
        return os.path.isdir(item)

    def 符合测试组名开头部分吗(self,item):
        if not isinstance(item,str):
            raise TypeError("must be str, not "+type(item).__name__)
        return item.startswith(self.测试组名开头部分)
    	  
    def 测试组内全是文件吗(self):
        import os
        return not any(os.path.isdir(i) for i in os.listdir())
    
    def 收录进测试组合集以相对路径(self,relativePath):
        if not isinstance(relativePath,str):
            raise TypeError("must be str, not "+type(relativePath).__name__)
        temp=[_ for _ in os.listdir() if os.path.isfile(_) and not _.startswith(".")]
        if len(temp)==2:self.测试组合集.append([os.sep.join([".",relativePath,i])\
for i in sorted(temp)])

    
    def 取测试组合集(self):
        for item in sorted(os.listdir()):
            if self.是目录吗(item) and self.符合测试组名开头部分吗(item):
                os.chdir(item)
                self.收录进测试组合集以相对路径(item)
                os.chdir("..")
                
    def 测试组合集存在有效测试组(self):
        for _ in self.测试组合集:
            if len(_)>1:return True
        return False
    
    def 测试组关卡(self,which):
        if not isinstance(which,int):raise TypeError("必须是整数")
        if which<1:raise ValueError("不能小于1")
        if which>len(self.测试组合集):
            raise ValueError("没有这么多组")
                  
    def 请输入测试第几组(self):
        which=int()
        while(True):
            answer=input("\n请输入测试第几组(Enter:返回):")
            if not answer:
                self.back=True
                return
            try:which=int(answer)
            except:continue
            try:self.测试组关卡(which)
            except Exception as e:
                print("❌"+type(e).__name__+":"+e.__str__())
                continue
            break
        return which

    def 测试第几组(self,which=None):
        if which==None:
            which=self.请输入测试第几组()
            if self.back:return
        else:
            try:self.测试组关卡(which)
            except:raise
        self.当前测试组=self.测试组合集[which-1]
        self.文件名1=self.当前测试组[0]
        self.文件名2=self.当前测试组[1]
        
    def 查看文件大小(self):
        print("🔎")
        for filename in self.当前测试组:
            print("文件大小:",os.path.getsize(filename),"字节",end=str())
            input()

    def 打开文件(self):
        self.文件1=open(self.文件名1)
        self.文件2=open(self.文件名2)
        
    def 获取文件内容(self):
        if True in [not type(f).__name__=="TextIOWrapper" for\
f in [self.文件1,self.文件2]]:
            raise TypeError("must be file")
        self.内容1=[f"这是哪个文件的：《{self.文件名1}》\n\n"]+[l.rstrip()+"\n" for l in self.文件1.readlines()]
        self.内容2=[f"这是哪个文件的：《{self.文件名2}》\n\n"]+[l.rstrip()+"\n" for l in self.文件2.readlines()]        

    def 关闭文件(self):
        self.文件1.close()
        self.文件2.close()

    def 找出不同之处(self):
        self.less=self.内容1
        self.more=self.内容2
        if not (isinstance(self.less,list) and isinstance(self.more,list)):
            raise TypeError("must be list")
        if len(self.less)>len(self.more):
            self.less,self.more=self.more,self.less
           
        differences=list()
        line=str()
        lineno=int()
        
        differences_more=list(set(self.more)-set(self.less))
        differences_less=list(set(self.less)-set(self.more))
        
        differences_more.sort()
        differences_less.sort()
      
            
        for line_more in differences_more:
            # 在原文内容开头加入n行时，以原文内容index+1-n作为行号。
            lineno=self.more.index(line_more)+1-1
            self.不同之处带行号_more.append((lineno,line_more))
        
        for line_less in differences_less:
            lineno=self.less.index(line_less)+1-1
            self.不同之处带行号_less.append((lineno,line_less))
            
            
        self.不同之处带行号_more=sorted(self.不同之处带行号_more,key=lambda current:current[0])
        self.不同之处带行号_less=sorted(self.不同之处带行号_less,key=lambda current:current[0])
        self.不同之处持有者_按行号排序=[self.不同之处带行号_more, self.不同之处带行号_less]
        
        self.不同之处带行号_more=sorted(self.不同之处带行号_more,key=lambda current:current[1])
        self.不同之处带行号_less=sorted(self.不同之处带行号_less,key=lambda current:current[1])        
        self.不同之处持有者_按内容排序=[self.不同之处带行号_more, self.不同之处带行号_less]
    
    
    def 输出不同之处带行号(self):
        with open("两个文件不同之处_按行号排序.txt","w") as f:
            f.write("\n🔎-Differences With Line Number(the more line file)-\n")
            for lineno,line in self.不同之处持有者_按行号排序[0]:
                f.write(f"{lineno} {line}")
            f.write("\n\n🔎-Differences With Line Number(the less line file)-\n")
            for lineno,line in self.不同之处持有者_按行号排序[1]:
                f.write(f"{lineno} {line}")
        
        
        with open("两个文件不同之处_按内容排序.txt","w") as f:
            f.write("\n🔎-Differences With Line Number(the more line file)-\n")
            for lineno,line in self.不同之处持有者_按内容排序[0]:
                f.write(f"{lineno} {line}")
            f.write("\n\n🔎-Differences With Line Number(the less line file)-\n")
            for lineno,line in self.不同之处持有者_按内容排序[1]:
                f.write(f"{lineno} {line}")
                        
    def 输出全文并标记不同之处(self):     
        with open("输出全文并标记不同之处_按行号排序.html","w") as f:
            不同之处行号集 = [ _[0] for _ in self.不同之处持有者_按行号排序[0]]
            f.write("<style> .red { color: red; } .blue { color: blue; } </style>")
            f.write("<pre>")
            # 第一个文件内容
            f.write("<div>🔎-Differences With Line Number(the more line file)-</div>")
            for index,line in enumerate(self.more):                
                lineno = index + 1 - 1                    
                if 不同之处行号集 and lineno == 不同之处行号集[0]:
                    f.write(f"<span class='red'>{lineno} {line}</span><br>")
                    不同之处行号集.pop(0)
                    continue
                f.write(f"{lineno} {line}<br>")
            
            # 下一个文件内容
            不同之处行号集 = [ _[0] for _ in self.不同之处持有者_按行号排序[1]]
            f.write("<div>🔎-Differences With Line Number(the less line file)-</div>")
            for index,line in enumerate(self.less):     
                lineno = index + 1 - 1
                if 不同之处行号集 and lineno == 不同之处行号集[0]:
                    f.write(f"<span class='blue'>{lineno} {line}</span><br>")
                    不同之处行号集.pop(0)
                    continue
                f.write(f"{lineno} {line}<br>")
            f.write("</pre>")
   
# - sub executed -
	
    def 开始游戏(self):
        while True:
            if (self.获取测试组父目录()=="EXIT"):return
            self.进入测试组父目录()
            self.获取测试组名开头部分()
            
            self.取测试组合集()
            input("🔎-Every Group-\n"+f"{self.测试组合集}")
            if not self.测试组合集存在有效测试组():
                input("❌没有有效的测试组，请重新选择。\n")
                self.测试组合集.clear()
                continue            
            break

        self.测试第几组()
        if self.back:
            self.重置()
            self.back=False           
            return
        
        input("\n🔎-Be Compared-\n"+f"{self.文件名1}\n{self.文件名2}\n")        

        self.查看文件大小()
        self.打开文件()
        self.获取文件内容()
        self.关闭文件()
        self.找出不同之处()
       
        self.输出不同之处带行号()
        
        self.输出全文并标记不同之处()
        
        self.重置()
 

def 测试两个文件不同之处():
    两个文件不同之处=两个文件不同之处世界("测试组")
    while (True):
        两个文件不同之处.开始游戏()
        if input("\n# Q/q to quit:").lower()=="q":break
        print()


def 主函数():
    测试两个文件不同之处()
    
    
if __name__=="__main__":主函数()



