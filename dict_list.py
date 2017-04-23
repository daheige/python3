#字典列表使用
aliens = [
    {
        'name':'daheige',
        'lang':'php'
    },
    {
        'name':'guangge',
        'lang':'mysql'
    },
    {
        'name':'maoge',
        'lang':'java'
    }
]
print(aliens)
for val in aliens:
    print(val)
    for name,lang in val.items(): #遍历字典的每一项用items()
        print(name+':'+lang)
pizza = {
    'name':'daheige',
    'books':['php','c++','nodejs','python'],
    'price':{
        'gold':123,
        'white':234,
        'black':45
    }
}
print(pizza)
print('---------books----------')
#遍历列表采用for...in方式
for book in pizza['books']:
    print(book)

for name,price in pizza['price'].items():
    print(name+':'+str(price))