#!/usr/bin/env python3
" Heos python lib "

import asyncio
from pprint import pprint

import aioheos


@asyncio.coroutine
def heos_test(loop):
    """ test heos """

    verbose = True 
    # host = None
    host = '192.168.11.31'
    username = 'jarlebh@gmail.com'
    password = 'Indgu966'

    heos = aioheos.AioHeosController(loop, host, username, password, verbose=verbose)

    # connect to player
    yield from heos.connect()


    heos.request_groups()
    heos.get_groups()[0].request_update()
    for _ in range(0, 20):
        favs = heos.get_favourites()    
        if len(favs) == 0:
            yield from asyncio.sleep(0.5)
    
    
    heos.request_now_playing_media(heos.get_players()[0].player_id)
    pprint(vars(heos.get_players()[0]))

    """ for fav in favs:
        if (fav['name'].find("P4") >= 0):
           pr
           int ("Playing {} from {}".format(fav['name'], fav)) """
    pids = []
    for player in heos.get_players():
        print ("Player {} pid {}".format(player.name, player.player_id))
        if (player.name.find("Kj") >= 0):
            pids.append(player.player_id)

    pprint(vars(heos.get_groups()[0]))
    #heos.set_group(heos._player_id, pids)

    #       heos.play_favourite(fav['mid'])
    # with open('hello.mp3', mode='rb') as fhello:
    #     content = fhello.read()
    # content_type = 'audio/mpeg'
    # heos.play_content(content, content_type)
    # heos.get_players()[0].stop()
    # print(heos.get_players()[0].source_list())
    # for fav in heos.get_players()[0].favourites_list():
    #     if fav['name']  == "NRK P1 Buskerud (Kongsberg)":
    #         heos.get_players()[0].play_favorite(fav['mid'])


    # do some work...
    heos.get_players()[0].create_group(["-2145613281", "-760835591"])
    yield from asyncio.sleep(10)
    heos.get_groups()[0].recreate_group()
    yield from asyncio.sleep(50)
    heos.close()


def main():
    " main "

    loop = asyncio.get_event_loop()
    heos_task = loop.create_task(heos_test(loop))
    try:
        loop.run_until_complete(heos_task)
    except KeyboardInterrupt:
        pass
        # for task in asyncio.Task.all_tasks():
        #     task.cancel()
    finally:
        loop.close()

if __name__ == "__main__":
    main()
