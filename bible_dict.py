#%%
import sys
import glob
import os


def main(input_list):
    find_key = "".join(input_list)
    if ':' not in find_key:
        find_key = input_list[0]+input_list[1]+":"+input_list[2]

    if len(input_list) > 3:
        print("입력 값이 너무 많습니다.")
        return

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