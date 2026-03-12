# 这两种不能直接换行，可以用方括号包在一起
mess1 = 'xxxxxxxxxxxxx'
mess2 = ("xxxxxxxxx"
         "xxxx")


# 输出结果：xxxxxxxxxxxxx
print(mess1)
# 输出结果：xxxxxxxxxxxxx
print(mess2)

# 可换行，可作为多行注释使用
mess3 = '''xxxxxxxxxxxxx'''
# 可换行，可作为多行注释使用，还能作为文档字符串使用
mess4 = """xxxxxxxxxxxxx"""