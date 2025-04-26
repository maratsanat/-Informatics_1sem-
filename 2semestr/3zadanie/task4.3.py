def prefix_to_word(prefix):
    if not prefix:
        return ''
    
    word = [''] * len(prefix)
    word[0] = 'A'  # Первый символ всегда 'A'
    
    for i in range(1, len(prefix)):
        if prefix[i] > 0:
            # Копируем соответствующий символ из префикса
            word[i] = word[prefix[i] - 1]
        else:
            # Собираем все запрещенные символы
            banned_chars = {'A'}  # Первый символ всегда запрещен
            k = prefix[i-1] if i > 0 else 0
            
            # Рекурсивно собираем все символы, которые могут создать префикс
            while k > 0:
                banned_chars.add(word[k])
                k = prefix[k-1]
            
            # Выбираем минимальную доступную букву (A-Z)
            for c in range(66, 91):  # От 'B' до 'Z'
                if chr(c) not in banned_chars:
                    word[i] = chr(c)
                    break
            else:
                # Если все буквы A-Z использованы, переходим на a-z
                for c in range(97, 123):
                    if chr(c) not in banned_chars:
                        word[i] = chr(c)
                        break
    
    return ''.join(word)

# Тестовые примеры
prefix1 = [0, 0, 2, 1, 0, 1]
print(prefix_to_word(prefix1))  