file = open('./external-files/10-words_sorted.txt', 'r')

def words_with_letters(words, letters):
  resTab = []
  for line in words:
    mot = line[:-1] # delete '\n' after words
    i = 0
    for let in mot:
      if let == letters[i]:
        i += 1
      if(i == len(letters)):
        resTab.append(mot)
        break
  words.seek(0)  # reset the cursor to the beginning of the file
  return resTab

print(words_with_letters(file, "klore"))
print(words_with_letters(file, "brohiic"))
print(words_with_letters(file, "azaz"))