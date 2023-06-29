count = 0
palindromes = []


# Проверка на палиндром. Фильтруем длину слов - минимум 3 буквы.
def is_palindrome(s) -> bool:
    if len(s) < 3:
        return False
    for i in range(int(len(s) / 2)):
        if s[i] != s[-1 - i]:
            return False
    return True


# Открываем файл, считываем слово и отправляем на проверку. Если да, добавляем в список.
with open('./russian.txt') as txt:
    s = txt.readline().replace('\n', '')
    while s != '':
        if is_palindrome(s):
            count += 1
            palindromes.append(s)
        s = txt.readline().replace('\n', '')

palindromes.sort(key=len)
palindromes = palindromes[::-1]

# Сохраняем список.
with open('palindromes.txt', 'w') as file:
    for palindrome in palindromes:
        file.write(f'{palindrome}\n')

# Выводим количество.
print(count)
