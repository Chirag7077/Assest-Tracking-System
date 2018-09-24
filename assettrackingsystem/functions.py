from assettrackingsystem import bcrypt

def create_connection():
    import pymysql
    
    conn = pymysql.connect(user="root",password="",host="localhost",database="asset_manager")
    cursor = conn.cursor()
    return conn, cursor

def authenticate(email, passwd):

    conn , cursor = create_connection()
    status = 0 
    try:
        cursor.execute("select user_id,passwd from users where email_id = '" + str(email) +"';")
        t = cursor.fetchone()
        if t:
            if passwd == t[1]:
                status = 1
                user_id = t[0]
                cursor.execute("select role from user_roles where user_id = '" + str(t[0]) +"';" )
                t2 = cursor.fetchall()
                roles = set()
                for i in t2:
                    roles.add(i[0])
                return status,roles,user_id
            else:
                return 0,None,None
        else:
            return 0,None,None
    finally:
        cursor.close()
        conn.close()

#roles = set()
#status, roles, id = authenticate("jalajlimaye@gmail.com","jalaj333")

