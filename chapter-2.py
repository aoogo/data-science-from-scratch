# _*_ coding: utf-8 _*_
import random

# 2.2.3 生成器和迭代器

# 每个dict都有一个item()方法可以返回它的键值对列表
# 更常见的做法是使用iteritems()方法：当我们在列表上迭代的时候它延迟yield为每次一个键值对

data = {'tom': 90, 'James': 78, 'Aurora': 92}
print data.items()  # [('James', 78), ('Aurora', 92), ('tom', 90)]
print data.iteritems()  # <dictionary-itemiterator object at 0x0000000003840C78>
print list(data.iteritems())  # [('James', 78), ('Aurora', 92), ('tom', 90)]

for i in data.iteritems():
    print i

# 2.2.4 随机性

four_uniform_randoms = [random.random() for _ in range(4)]
print four_uniform_randoms
# [0.1166468443461508, 0.3601295226651432, 0.895136448213768, 0.9245333586487791]

# random.seed(10)  # 设置随机数种子为10
print random.random()   # 0.57140259469
# random.seed(10)
print random.random()   # 0.57140259469

print random.randrange(10)
print random.randrange(3, 6)

up_to_ten = range(10)
print up_to_ten
random.shuffle(up_to_ten)
print up_to_ten

# 从列表随机取一个元素
my_best_friend = random.choice(["Alice", "Bob", "Charlie"])
print my_best_friend

four_with_replacement = [random.choice(range(10)) for _ in range(4)]
print four_with_replacement

# 2.2.7 函数式工具


def exp(base, power):
    return base ** power


# def two_to_the(power):
#     return exp(2, power)


# print two_to_the(3)

from functools import partial
two_to_the = partial(exp, 2)   # 现在是一个包含一个变量的函数
print two_to_the(3)    # 8

square_of = partial(exp, power=2)
print square_of(3)    # 9


def double(x):
    return 2 * x


xs = [1, 2, 3, 4]
# twice_xs = [double(x) for x in xs]
# twice_xs = map(double, xs)
# print twice_xs

list_douber = partial(map, double)
twice_xs = list_douber(xs)
print twice_xs


def multiply(x, y):
    return x * y


products = map(multiply, [1, 2], [4, 5])    # [4, 10]
print products


def is_even(x):
    return x % 2 == 0


# x_evens = [x for x in xs if is_even(x)]     # [2, 4]
# x_evens = filter(is_even, xs)      # [2, 4]
list_evener = partial(filter, is_even)
x_evens = list_evener(xs)

print x_evens

x_product = reduce(multiply, xs)
print x_product
list_product = partial(reduce, multiply)
x_product = list_product(xs)
print x_product

# 2.2.9
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
print zip(list1, list2)     # [('a', 1), ('b', 2), ('c', 3)]

pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)
print letters
print numbers


def add(a, b):
    return a+b


print add(1, 2)
# print add([1, 2])   # TypeError
print add(*[1, 2])

# 2.2.10 args和kwargs


def magic(*args, **kwargs):
    print "未命名参数:", args
    print "关键词参数:", kwargs


magic(1, 2, key="word", key2="word2")
# 未命名参数: (1, 2)
# 关键词参数: {'key2': 'word2', 'key': 'word'}


def other_way_magic(x, y, z):
    return x+y+z


x_y_list = [1, 2]
z_dict = {"z": 3}
print other_way_magic(*x_y_list, **z_dict)  # 6


