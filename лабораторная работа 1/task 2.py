# TODO Найдите количество книг, которое можно разместить на дискете
pages = 100
lines = 50
symbols = 25
bytes = 4
size = 1.44 * 1024 * 1024
book = pages * lines * symbols * bytes
numbers = size // book

print("Количество книг, помещающихся на дискету:", int(numbers))
