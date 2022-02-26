from pprint import pprint
import rds_config
import pymysql

class client:
    def __init__(self):
        # initialise MySQL database credentials from file
        self.rds_host  = rds_config.db_endpoint
        self.name = rds_config.db_username
        self.password = rds_config.db_password
        self.db_name = rds_config.db_name
        self.port = 3306

        # connect
        self.conn = self.__conn__()

    def __conn__(self):
        '''
        Connect to the database using credentials from config file
        '''

        # return connection
        return pymysql.connect(host=self.rds_host, 
                                user=self.name, 
                                password=self.password,
                                db=self.db_name,
                                cursorclass=pymysql.cursors.DictCursor)

    def query(self, queryString):
        '''
        Get query response from input query string
        '''

        # use cursor for query
        with self.conn.cursor() as cur:
            
            # execute the query (stored in cursor)
            cur.execute(queryString)

            # get query result from cursor
            rows = cur.fetchall()

            # return result as dictionary
            return rows


# example operation of class
if __name__ == '__main__':

    # initialise client with connection
    cl = client()

    # run a query
    response = cl.query('SELECT * FROM crowd')

    # close connection (don't leave open!)
    cl.conn.close()

    # print result
    pprint(response)