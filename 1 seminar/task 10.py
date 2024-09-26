with open("input.txt", "r") as f:
    a = f.read()
k = f
c = ['б', 'в', 'г', 'л', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']
g = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
for i in range(1, len(a)-1):
    if (((a[i-1] in c) or (a[i-1] == ' ')) and (a[i] in g) and ((a[i+1] in c) or (a[i+1] == ' '))):
         k = k.replace(a[i], a[i] + 'с' + a[i])
print(k)