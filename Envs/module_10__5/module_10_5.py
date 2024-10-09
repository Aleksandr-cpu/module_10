import multiprocessing
import datetime

# Вывод в консоль без multiprocessing: 0:00:02.953041
# Вывод в консоль c multiprocessing: 0:00:01.214486


def read_info(name):
    all_data = []
    with open(name, 'r', encoding="UTF-8") as f:
        for line in f:
            line = f.readline()
            if line != "":
                all_data.append(line.strip())

filenames = [f'./file {number}.txt' for number in range(1, 5)]
# start = datetime.datetime.now()
# for file in filenames:
#     read_info(file)
# end = datetime.datetime.now()
# print(end - start)

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        start = datetime.datetime.now()
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(end - start)