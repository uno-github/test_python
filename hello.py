import io , sys ,locale
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# print(sys.getdefaultencoding())
# print(sys.stdout.encoding)

a = 123
b = "日本語"

print(a)
print(b)

for val in ['aaa','bbb','ccc']:
    print(val)


def func_hoge (n):
    if n > 1 :return True
    return False

print(func_hoge(3))

1 + 3