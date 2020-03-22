import gspread
from przlist import rank_query
from oauth2client.service_account import ServiceAccountCredentials
scope= ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]  
credential=ServiceAccountCredentials.from_json_keyfile_name("C:/Users/Junior Sosa/Desktop/python_projects/my_sheets_api_project/creds.json",scope)
client= gspread.authorize(credential)
comp=client.open_by_key("1QT_mHHZRGqNVAsDB8TQchBOhEsFJvb1IhzTJtD0GmCY").get_worksheet(1)
estcde=comp.range('J259:J325')
clsroomps=comp.range('N259:N325')
bathps=comp.range('O259:O325')
equipps=comp.range('P259:P325')
othspps=comp.range('Q259:Q325')
for a,b,c,d,e in zip(estcde,equipps,clsroomps,bathps,othspps):
    if d.value =='' or b.value=='' or c.value=='' or e.value=='':
        ps=rank_query(a.value)
        b.value= ps[0]
        c.value= ps[1]
        d.value= ps[2]
        e.value= ps[3]
comp.update_cells(equipps)
comp.update_cells(clsroomps)  
comp.update_cells(bathps)      
comp.update_cells(othspps)