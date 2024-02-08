# encoding='utf-8'

import os,json,base64

tvbox = dict()

def createJsonFile(fileName='h'):
    jarName = 'clan://TVBox/'+fileName+'.jar'
    liveName = 'clan://TVBox/'+fileName+'.txt'
    print('jarName: '+jarName+ '--- liveName: '+liveName)
    
    tvbox['spider'] = jarName
    tvbox['lives'] = dict()
    tvbox['lives']['channels'] = dict()
    tvbox['lives']['group'] = 'redirect'
    tvbox['lives']['channels']['name'] = 'redirect'
    lt = base64.b64encode(liveName.encode('utf-8')).decode('utf-8')
    tvbox['lives']['channels']['urls'] = 'proxy://do=live&type=txt&ext='+lt
        
    with open(fileName+'.json','w',encoding='utf-8') as f:
        json.dump(tvbox,f,indent=1,ensure_ascii=False)

def fusion(file):
    load_dict = json.load(file)
    if load_dict.__contains__('wallpaper'):
        tvbox.setdefault('wallpaper',load_dict['wallpaper'])
    if load_dict.__contains__('ijk'):
        tvbox.setdefault('ijk',load_dict['ijk'])
    if load_dict.__contains__('ads'):
        if tvbox.__contains__('ads'):
            tvbox['ads'] = list(set(tvbox['ads']+load_dict['ads']))
        else:
            tvbox['ads'] = load_dict['ads']
    if load_dict.__contains__('flags'):
        if tvbox.__contains__('flags'):
            tvbox['flags'] = list(set(tvbox['flags']+load_dict['flags']))
        else:
            tvbox['flags'] = load_dict['flags']
    # 解析器
    # if load_dict.__contains__('parses'):
    #     for parse in load_dict['parses']:
    #         print(parse['url'])
    # 网站
    if load_dict.__contains__('sites'):
        site_fliter(load_dict['sites'])
        
def site_fliter(sites):
    for site in sites:
        print(site)
    
            
if __name__ =='__main__':
    for root,dir,files in os.walk('./json'):
        for file in files:
            if '.json' in os.path.abspath(file):
                with open(os.path.join(root,file),encoding='utf-8') as f:
                    fusion(f)     
    createJsonFile('b')