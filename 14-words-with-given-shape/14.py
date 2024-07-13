file = open('./external-files/words_sorted.txt', 'r')

def words_with_given_shape(words, shape):
  res = []
  for word in words:
    word = word[:-1]
    if len(word) == len(shape)+1:
      i = 1
      stop = False
      while i <= len(shape) and not stop:
        diffLet = ord(word[i]) - ord(word[i-1])
        if diffLet != 0:
          diffLet /= abs(diffLet)
        if diffLet != shape[i-1]:
          stop = True
        i+=1
      if not stop:
        res.append(word)
  words.seek(0)  # reset the cursor to the beginning of the file      
  return res
        
    

print(words_with_given_shape(file, [1, -1, -1, -1, 0, -1]))
print(words_with_given_shape(file, [1, -1, -1, 0, -1, 1]))
print(words_with_given_shape(file, [0, 1, -1, 1]))
print(words_with_given_shape(file, [1, 1, 1, 1, 1, 1, 1]))