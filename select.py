import cx_Oracle
from ConfigManager import ConfigManager

def Select_trap():
    ob = ConfigManager()
    con = cx_Oracle.connect(ob.getDBConnection())
    cur = con.cursor()
    trap = {'lowVolatage','fanStatus Fail','temp Hight','linkDown','shutDown','coldStart','hardReset','CRC Frame','DDos detected','hard Reset','fanFail'}
    Id = raw_input("please input devices CLLI: ")
    cur.execute("select TRAP from SYSTEM.TRAP WHERE IDDEVICE=:Id",{'Id':Id})
    data = cur.fetchall()
    if data == []:
        print 'No such device in DB'
    else:
        print 'Errors: '
        for row in data :
            if row[0] in trap:
                print row[0]
    cur.close()
    con.close()

Select_trap()

