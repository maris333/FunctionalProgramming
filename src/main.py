def main():
    add_fifteen = lambda x: x + 15
    print(add_fifteen(10))
    product = lambda x, y: x / y
    print(product(10, 2))
    to_sort = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
    to_sort.sort(key=lambda x: x[1])
    print(to_sort)
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    squares = list(map(lambda x: x ** 2, my_list))
    print(squares)
    cubes = list(map(lambda x: x ** 3, my_list))
    print(cubes)
    lines = ["10000101011", "111111", "01010101010010", "011001100001", "001010101011"]
    filtered = len(list(filter(lambda x: not "11" in x, lines)))
    print(filtered)
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    nums3 = [7, 8, 9]
    sum_nums = sum(list(map(lambda x, y, z: x + y + z, nums1, nums2, nums3)))
    print(sum_nums)
    colors = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
    strings = list(map(lambda x: ' '.join(x), colors))
    print(strings)
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even = list(map(lambda z: z ** 2, list(filter(lambda x: x % 2 == 0, nums))))
    print(even)
    orders = [
        ["34587", "Learning Python, Mark Lutz", 4, 40.95],
        ["98762", "Programming Python, Mark Lutz", 5, 56.80], ["77226", "Head First Python, Paul Barry", 3, 32.95],
        ["88112", "Einführung in Python3, Bernd Klein", 3, 24.99]
    ]
    invoice = list(map(lambda x: (x[0], x[3] * x[2] if x[3] * x[2] > 100 else x[3] * x[2] + 10), orders))
    print(invoice)


if __name__ == main():
    main()
