# Get user input

file = input('File name: ').lower()

# Print file category and type

if '.gif' in file:
    print('image/gif')
elif '.jpeg' in file:
    print('image/jpeg')
elif '.jpg' in file:
    print('image/jpg')
elif '.png' in file:
    print('image/png')
elif '.zip' in file:
    print('application/zip')
elif '.pdf' in file:
    print('application/pdf')
elif '.txt' in file:
    print('text/plain')
else:
    print('application/octet-stream')



