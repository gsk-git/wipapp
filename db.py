import uuid
import sqlalchemy
from google.cloud.sql.connector import Connector
# initialize connector
connector = Connector()

# getconn now set to private IP
def getconn():
    conn = connector.connect(    )
    return conn

# create connection pool
pool = sqlalchemy.create_engine("mysql+pymysql://", creator=getconn)

insert_q = sqlalchemy.text("INSERT INTO Users(UUID,LastName,FirstName,EmailID,City,Gender,Mobile,PassD)\
                            VALUES (:UUID,:LastName,:FirstName :EmailID,:City,:Gender,:Mobile,:PassD)")
insert_v = {
            "UUID":str(uuid.uuid4()),
            "LastName":lname,
            "FirstName":fname,
            "EmailID":email, 
            "City":city,
            "Gender":gen,
            "Mobile":mob,
            "PassD":pswd
            }

# connect to connection pool
with pool.connect() as db_conn:
    # query database and fetch results
    results = db_conn.execute(sqlalchemy.text("SELECT * FROM Users")).fetchone()
    db_conn.execute(sqlalchemy.text(insert_q, parameters=insert_v))
    db_conn.commit()
    print(results)

# cleanup connector
connector.close()
