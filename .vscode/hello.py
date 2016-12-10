
# print('hello python 日本語!')
import io , sys ,locale

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print(sys.getdefaultencoding())
print(sys.stdout.encoding)
print('こんにちはこんにちは')



