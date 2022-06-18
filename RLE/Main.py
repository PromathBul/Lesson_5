def rle_encode(data_input):
    encoding = ''
    count = 1
    if not data_input:
        return ''
    for ind in range(1, len(data_input)):
        if data_input[ind] == data_input[ind - 1]:
            count += 1
        else :
            encoding += str(count) + data_input[ind - 1]
            count = 1
    else:
        encoding += str(count) + data_input[ind - 1]
    return encoding

def rle_decode(data_output):
    decoding = ''
    count = ''
    for char in data_output:
        if char.isdigit():
            count += char
        else :
            temp = int(count) * char
            decoding += temp
            count = ''
    return decoding

def write_file(value, file):
    with open (file, 'w') as data:
        data.writelines(value)

file = 'Lesson_5\RLE\Data_input.txt'
data_input = ''
with open (file, 'r') as data:
    data_input = data.read()
print(f'Исходная информация в виде: {data_input}')

encode = rle_encode(data_input)
print(f'Информация в сжатом виде: {encode}')

file = 'Lesson_5\RLE\Data_encoding.txt'
write_file(encode, file)
print('Сжатая информация записана в файл \'Data_encoding.txt\'')

with open (file, 'r') as data:
    encode = data.read()
decode = rle_decode(encode)
file = 'Lesson_5\RLE\Data_output.txt'
write_file(decode, file)
print(f'Декодированная информация в виде: [{decode}] записана в файл \'Data_output.txt\'')