import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for number in range(1,6):
        await asyncio.sleep(10/power)
        print(f'Силач {name} поднял {number} шар')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Василий',9))
    task2 = asyncio.create_task(start_strongman('Федор', 7))
    task3 = asyncio.create_task(start_strongman('Иван', 5))
    await task1
    await task2
    await task3
    print('Соревнование завершено')

asyncio.run(start_tournament())
