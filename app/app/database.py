import sqlite3

#Open database
conn = sqlite3.connect('/Users/lol/Downloads/bbc-main2/app/database.db')
#Create table
conn.execute("Drop Table registerrr")
conn.execute('''
CREATE TABLE registerrr 
		(userId INTEGER PRIMARY KEY, 
		
		password TEXT,
		name TEXT,
		email TEXT
		)''')
conn.execute("Drop Table user")	
conn.execute('''CREATE TABLE user(
	product_id INTEGER,
	product_name TEXT,
	product_price TEXT,
	product_url TEXT,
	product_desc TEXT,
	total INTEGER,
	cum_total INTEGER
)''')
conn.execute("Drop Table details")

conn.execute('''CREATE TABLE details(
	detail_images TEXT
)''')
conn.execute("Drop Table wishlist")
conn.execute('''CREATE TABLE wishlist 
	(product_id INTEGER)''')
conn.execute("Drop Table cart")
conn.execute('''CREATE TABLE cart
	(product_id INTEGER,
	userId INTEGER,
	size TEXT,
	quantity INTEGER)''')
conn.close()
