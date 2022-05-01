#%%
import sys
import glob
import os


def main(input_list):
    if len(input_list) == 1:
        for i in range(len(input_list[0])):
            if input_list[0][i] in ['1','2','3','4','5','6','7','8','9']:
                break
        book_name = input_list[0][:i]
        jang = input_list[0].split(':')[0][i:]
        jul = input_list[0].split(':')[1] 

    elif len(input_list) == 2:
        book_name = input_list[0]
        jang = input_list[1].split(':')[0]
        jul = input_list[1].split(':')[1]

    elif len(input_list) == 3:
        book_name = input_list[0]
        jang = str(input_list[1])
        jul = str(input_list[2])
        
        
    # if book_name in name_long2short:
    #     book_name = name_long2short[book_name]
    
    assert book_name in book_name_dict, book_name+" - 권 이름이 잘 못 됐습니다"
    file_name = book_name_dict[book_name]
    find_key = book_name+jang+":"+jul

    count = 0
    error = True
    with open(file_name, encoding='cp949') as f:
        book_string = f.read()
        book_split = book_string.split('\n')
        for lines in book_split:
            key = lines.split(' ')[0]
            if (key == find_key or count > 0):
                print(lines)
                count += 1
                error = False
                if count == 5:
                    break

    if error == True:
        print("입력 값을 다시 확인해주세요 : ", find_key)



if __name__ =="__main__":
    book_name_dict = {}
    name_long2short = {}
    file_list = glob.glob('text/*.txt')
    for file_name in file_list:
        key1 = os.path.basename(file_name).split('.')[0][4:]
        line = open(file_name, encoding='cp949').readline()
        key2 = line.split('1')[0]

        book_name_dict[key1] = file_name
        book_name_dict[key2] = file_name
        name_long2short[key1] = key2


    if len(sys.argv) == 1:
        while 1:
            input_list = input('\n검색 내용을 입력하세요: ').split()
            main(input_list)

    else:
        input_list = sys.argv[1:]
        main(input_list)