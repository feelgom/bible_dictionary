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
        
    find_key = book_name+jang+":"+jul

    count = 0
    error = True
    with open('bible.txt', encoding='cp949') as f:
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
    if len(sys.argv) == 1:
        while 1:
            input_list = input('\n검색 내용을 입력하세요: ').split()
            main(input_list)

    else:
        input_list = sys.argv[1:]
        main(input_list)