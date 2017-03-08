
'''

    

'''

import os
import os.path

cmd = "luacheck %s"
def get_all_pathname(path,suffix):
    '''
        获取指定文件夹下 特定后缀的所有文件全路径
    '''
    result = []
    for parent, dirnames,filenames in os.walk(path):
        for filename in filenames:
            if os.path.splitext(filename)[1] == suffix:
                result.append(os.path.join(parent,filename))
    return result

def check_lua_file(fullName):
    r = os.popen(cmd%fullName)
    text = r.read()
    r.close()

    result = []
    for line in text.splitlines():
        if len(line) > 0 and line.find("Checking") ==-1 and line.find("Total") == -1:
            result.append(line)
    return result

def main():
    '''
    print("hello")
    r =os.popen(cmd)
    text = r.read()
    r.close()
    print(text)
    '''
    cur_path = os.getcwd()
    pathname = get_all_pathname(cur_path,".lua")

    for path in pathname:
        print("-----------------------------------")
        result = check_lua_file(path)
        print(result)
        #text = "%s >> %s"%(path,0)
        #print(text)
    
if __name__ == "__main__":
    main()
    input("input any key to continue!")
