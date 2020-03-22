import gspread
from pprint import pprint
from oauth2client.service_account import ServiceAccountCredentials
scope= ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]  
credential=ServiceAccountCredentials.from_json_keyfile_name("C:/Users/Junior Sosa/Desktop/python_projects/my_sheets_api_project/creds.json",scope)
client= gspread.authorize(credential)
prznlist19 = client.open_by_key('1dYTYqWazRL4-WRSpkSkI46ly1wLTl7I_JJJ6vo74_xA')

equip=prznlist19.get_worksheet(0).get('B16:C75')
clrm=prznlist19.get_worksheet(1).get('B17:C76')
brm=prznlist19.get_worksheet(2).get('B17:C76')
ospc=prznlist19.get_worksheet(3).get('B19:C78')
def getps(code,list):
    for i in list:
        if len(i)==2:
            if i[1]==code:
                return i[0]
def rank_query(est_code):
    # checking if there's only one record with that code
    ab=sum([a[1] == est_code for a in equip if len (a)==2]) ==1
    bb=sum([b[1] == est_code for b in clrm if len (b)==2]) ==1
    cb=sum([c[1] == est_code for c in brm if len (c)==2]) ==1
    db=sum([d[1] == est_code for d in ospc if len(d)==2]) ==1
    if ab and bb and cb and db:
        return (getps(est_code,equip),getps(est_code,clrm),getps(est_code,brm),getps(est_code,ospc))
    else:
        return(0,0,0,0)
# print(prznlist19.get_worksheet(0).title,prznlist19.get_worksheet(1).title,prznlist19.get_worksheet(2).title,prznlist19.get_worksheet(3).title)   