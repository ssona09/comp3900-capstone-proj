import mysql.connector
# Establish the connection
# Just copy paste this to connect to the database
import pathlib
def get_ssl_cert():
    current_path = pathlib.Path(__file__).parent.parent
    return str(current_path / 'BaltimoreCyberTrustRoot.crt.pem')

conn = mysql.connector.connect(
  user = 'superstars@youdelish', 
  password = 'superstaR1!', 
  host = 'youdelish.mysql.database.azure.com', 
  database = 'project',
  ssl_ca=get_ssl_cert()
)

cursor = conn.cursor()


# Setting up the databases down here
# Initialise User Database

cursor.execute("INSERT INTO Customer (username, password, email, address) VALUES (%s, %s, %s, %s)", ("user1", "password", "user1@youdelish.com", "29 Joke Street, Joke 2000"))
cursor.execute("SELECT * from Cart_Item")
rows = cursor.fetchall()
for row in rows:
  print(row)