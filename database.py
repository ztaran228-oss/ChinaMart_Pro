import aiosqlite

DB_NAME = "database.db"

async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute('CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, role TEXT DEFAULT "user")')
        await db.execute('CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY AUTOINCREMENT, seller_id INTEGER, title TEXT, price REAL, description TEXT)')
        await db.commit()
        await db.execute('''
    CREATE TABLE IF NOT EXISTS cart (
        user_id INTEGER,
        product_id INTEGER
    )
''')

async def register_user(user_id):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute('INSERT OR IGNORE INTO users (user_id, role) VALUES (?, "user")', (user_id,))
        await db.commit()

async def get_role(user_id):
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute('SELECT role FROM users WHERE user_id = ?', (user_id,)) as cursor:
            row = await cursor.fetchone()
            return row[0] if row else 'user'

async def set_role(user_id, role):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute('UPDATE users SET role = ? WHERE user_id = ?', (role, user_id))
        await db.commit()