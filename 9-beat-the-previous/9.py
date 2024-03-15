

def extract_increasing(digits):
  digits = str(digits)
  i = 0
  tab = [int(digits[0])]
  while i <= len(digits):
    i += 1
    suiv = digits[i]
    while tab[-1] >= int(suiv):
      i += 1
      if i >= len(digits):
        return tab
      suiv += digits[i]
    tab.append(int(suiv))
  return tab

print(extract_increasing('600005'))
print(extract_increasing('045349'))
print(extract_increasing('77777777777777777777777'))
print(extract_increasing('1234' * 100))