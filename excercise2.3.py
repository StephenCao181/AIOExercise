import gdown

url = 'https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko'  
output = 'P1_data.txt'  # Đặt tên file bạn muốn lưu
gdown.download(url, output, quiet=False)

with open('P1_data.txt', 'r') as f:
    document = f.read()

words = document.split()

counter = {}
for word in words:
    if word in counter:
        counter[word] += 1
    else:
        counter[word] = 1

print(counter)
