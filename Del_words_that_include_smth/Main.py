subtxt = 'ко'

txt = 'Абвер стал называть алфавит абвгдейкой'
print(txt)

lst = txt.lower().split()
new_txt =' '.join([i for i in lst if not subtxt in i])

print(new_txt)