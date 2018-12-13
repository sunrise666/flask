#encoding: utf-8
#mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = 'sunrise'
HOST = 'localhost'
PORT = '3306'
DATABASE = 'db_demo1'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,
                                                                       DRIVER,USERNAME,PASSWORD,HOST,
                                                                       PORT,DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False
VARIABLE_VALUE = False