import mysql.connector

def connection():
    #establishing the connection
    conn = mysql.connector.connect(
        user='python', 
        password='adminadmin', 
        host='127.0.0.1', 
        database='python_imagenes'
    )
    return conn

def closeConnection(conn):
    try:
        # Closing the connection
        conn.close()
    except:
        print("error en conexion")
    return True

def dbinser():
    conn = connection()
    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    # Preparing SQL query to INSERT a record into the database.
    insert_stmt = (
   "INSERT INTO tbl_imagenes(imagenes_nombre,imagenes_texto,imagenes_ruta)"
   "VALUES (%s, %s, %s)"
    )
    data = ('nombre', 'texto', 'c:')
    try:
        # Executing the SQL command
        cursor.execute(insert_stmt, data)
        # Commit your changes in the database
        conn.commit()
        print("Data inserted")
    except:
        # Rolling back in case of error
        conn.rollback()
        print ("Exception")
    if closeConnection(conn): 
        print("closed connection")
    else: 
        print("error")

