import pymysql
def get_conn():
    host = "localhost"
    port = 3306
    db = "jdbc"
    user = "root"
    password = "843800695"
    conn = pymysql.connect(host=host,
                           user=user,
                           password=password,
                           db=db,
                           port=port,
                           charset="utf8")
    return conn

class User(object):
    def __init__(self,id ,name,password,blance,date):
        self.id = id
        self.name = name
        self.password = password
        self.blance = blance
        self.date = date
    # def save(self):
    #     conn = get_conn()
    #     cursor = conn.cursor()
    #     sql = "insert into user (user_id,user_name) VALUES (%s,%s)"
    #     cursor.execute(sql, (self.user_id,self.user_name))
    #     conn.commit()
    #     cursor.close()
    #     # conn.close()

    @staticmethod
    def query_all():
        conn = get_conn()
        cursor = conn.cursor()
        sql = "select * from user"
        # sql = "select * from user"
        cursor.execute(sql)
        rows = cursor.fetchall()
        users=[]
        for r in rows:
            user = User(r[0],r[1],r[2],r[3],r[4])
            users.append(user)
        conn.commit()
        cursor.close()
        conn.close()
        return  users
    # def __str__(self):
    #     return  "id:{} - name:{} - password:{} - blance:{} - date:{}".format(self.id,self.name,self.password,self.blance,self.date)
