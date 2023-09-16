import sqlite3 as sq
from create_bot import dp, bot

base = sq.connect('shop_cool.db')
cur = base.cursor()


def sql_start():
    global base, cur
    base = sq.connect('shop_cool.db')
    cur = base.cursor()
    if base:
        print('Data base connected!')
    base.execute('CREATE TABLE IF NOT EXISTS shop(img TEXT, product_id TEXT, description TEXT, price INTEGER)')
    base.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, user_id TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS cart(user_id INTEGER, name TEXT, quantity INTEGER, count INTEGER)')
    base.commit()
     
async def sql_add_command(state):
    async with state.proxy() as data_ad:
        cur.execute('INSERT INTO shop VALUES(?, ?, ?, ?)', tuple(data_ad.values()))
        base.commit()
        
async def sql_read(message):
    for ret in cur.execute('SELECT * FROM shop').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],f'{ret[1]}\nDescription: {ret[2]}\nPrice: {ret[-1]}')

async def sql_read2():
    return cur.execute('SELECT * FROM shop').fetchall()

async def sql_delete_command(data_ad):
    cur.execute('DELETE FROM shop WHERE product_id = ?', (data_ad, ))
    base.commit()
    
########################################################

class DataBase:
    def __init__(self, db_file):
        self.connect = sq.connect(db_file)
        self.cursor = self.connect.cursor()
        
    async def add_users(self, id, user_id):
        with self.connect:
            return self.cursor.execute(""" INSERT INTO users(id,user_id)VALUES(?, ?)""") 
        
    async def get_products(self):    #prendere prodotti dallo shop
        with self.connect:
            return self.cursor.execute(""" SELECT * FROM shop""").fetchall()
        
    async def get_user_product(self, product_id):
        with self.connect:
            return self.cursor.execute(""" SELECT * FROM shop WHERE product_id=(?)""", [product_id]).fetchall()
        
    async def get_cart(self, user_id):
        with self.connect:
            return self.cursor.execute(""" SELECT * FROM cart WHERE user_id=(?)""", [user_id]).fetchall()
        
    async def add_to_cart(self, user_id, product_id):
        with self.connect():
            return self.cursor.execute(""" INSERT INTO cart(user_id. product_id, count) VALUES(?, ?, ?)""", [user_id, product_id, 1]).fetchall()
        
    async def empty_cart(self, user_id):
        with self.connect:
            return self.cursor.execute(""" DELETE FROM cart WHERE usere_id=(?)""", [user_id])
        
    async def get_count_in_cart(self, user_id, product_id):
        with self.connect:
            return self.cursor.execute(""" SELECT count FROM cart WHERE user_id=(?) AND product_id=(?)""", [user_id, product_id]).fetchall()
        
    async def remove_on_item(self, product_id, user_id):
        with self.connect:
            return self.cursor.execute("""DELETE count FROM cart WHERE product_id=(?) AND user_id=(?)""", [user_id, product_id])
    
    async def change_count(self, count, user_id, product_id):
        with self.connect:
             return self.cursor.execute("""UPDATE cart SET count=(?) WHERE product_id=(?) AND user_id=(?)""", [count, user_id, product_id])
     
    
'''
async def add_to_cart(product_name, user_id):
    cur.execute('INSERT INTO cart(user_id, name) VALUES(?, ?)', (user_id, product_name))
    base.commit()
    
def create_tables():
    base = sq.connect('shop_cool.db')
    cur = base.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, user_id TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS cart(user_id INTEGER, name TEXT, quantity INTEGER)')
    base.commit()
    base.close()

async def get_cart(user_id):
    query = "SELECT name, quantity FROM cart WHERE user_id = ?"
    cur.execute(query, (user_id,))
    cart = cur.fetchall()
    cur.close()
    return [dict(name=product[0], quantity=product[1]) for product in cart]

async def empty_cart(user_id):
    try:
        cur.execute('DELETE FROM cart WHERE user_id = ?', (user_id,))
        base.commit()
    except sq.Error as e:
        print(f"Errore durante l'eliminazione dal database: {e}")
  
'''