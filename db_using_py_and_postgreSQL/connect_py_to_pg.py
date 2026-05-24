import psycopg2
import psycopg2.extras

hostname = "localhost"
database = "students"
username = "postgres"
pw = "1234"
port = 5432
conn = None
curr = None
try:
    with psycopg2.connect( host = hostname,
                            dbname = database,
                            user = username,
                            password = pw,
                            port = port) as conn:


        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as curr:  # need to create cursor to eatablish sql transactions.
                                                                              # psycopg2.extras.DictCursor will return the response in dictionary form.


            curr.execute('DROP TABLE IF EXISTS student')
            create_table_script = ''' CREATE TABLE IF NOT EXISTS student (
                                        id      int PRIMARY KEY,
                                        name    VARCHAR(40) NOT NULL,
                                        dept    VARCHAR(50) NOT NULL,
                                        dept_id VARCHAR(50) NOT NULL)'''
            
            curr.execute(create_table_script) 


            insert_script = 'INSERT INTO student (id, name, dept, dept_id) VALUES(%s,%s,%s,%s)'
            insert_values= [(1,"Thanos" , "MCA", "CS-01"),
                            (2,"Iron Man" , "B.Sc. in Maths", "Math-01"),
                            (3,"Iron Woman" , "class-3", "C-01"),
                            (4,"The Rock" , "MBBS", "MBBS-01"),
                            (5,"Randy" , "Never been to school", "NO-01"),
                            (6,"Orton" , "MBBS", "MBBS-01"),
                            (7,"John Cena" , "BA", "BA-01")]

            for listt in insert_values:
                curr.execute(insert_script, listt)

            # update scripts
            update_script = 'UPDATE student SET id = id + 1000'
            curr.execute(update_script)

            # delete script

            delete_script = 'DELETE FROM student WHERE name = %s'
            delete_val = ('Orton',)

            curr.execute(delete_script, delete_val)

            # show table
            curr.execute('SELECT * FROM student')
            for i in curr.fetchall():
                print(i['name'],"->", i['dept_id'])

            
            


    
    
except Exception as error:
    print(error)
finally:
    if conn is not None:
        conn.close()