SECRET_KEY = 'something random'
DEBUG = True

DB_HOST = 'sql3.freesqldatabase.com'
DB_USERNAME = 'sql3233839'
BLOG_DB_NAME = 'sql3233839'
DB_PASSWORD = 'REEwreYmFL'
DB_PORT = 3306
DB_URI = "mysql+pymysql://%s:%s@%s:%s/%s" % (DB_USERNAME,DB_PASSWORD,DB_HOST,DB_PORT,BLOG_DB_NAME)

SQLALCHEMY_DATABASE_URI = DB_URI