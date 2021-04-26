import aiohttp
import asyncio

class Async_User():
    def __init__(self):
        self.sess = aiohttp.ClientSession()

    async def get_user_by_username(self, username):
        async with self.sess.get('https://ReplREST.lamaqdahodwala.repl.co/api/user/{}'.format(username)) as resp:
            x = await resp.json()
            return x

    async def get_board(self, boardname):
        async with self.sess.get()