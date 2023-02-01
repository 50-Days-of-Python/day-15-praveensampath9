#Write your code here.
num = eval(input())
format_num = []
for i in num:
    x="{:,}".format(i) 
    format_num.append(str(x))
print(format_num)
