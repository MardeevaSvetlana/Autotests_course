# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt



story = open('test_file/task1_data.txt', 'r', encoding='utf-8')
new_story = open('test_file/task1_answer.txt', mode='w+', encoding='utf-8')
story1 = story.read()
new_story.write(''.join((x for x in story1 if not x.isdigit())))
new_story.close()
story.close()


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
