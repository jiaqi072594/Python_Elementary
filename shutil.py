#shutil(或成为shell工具)模块中包含一些函数，让你在Python程序中复制、移动、改名和删除文件。
'''
#复制文件和文件夹
    调用shutil.copy(source,destination),将路径source处的文件复制到路径destination出的文件夹（而这皆为字符串）。如果destination是一个文件名，它将作为被复制文件的新名字。该函数返回一个字符串，表示被复制文件的路径。
    shutil.copytree()将复制整个文件夹，以及它包含的文件夹个文件。调用shutil.copytree(source,destination),将路径source处的文件夹，包括他的所有文件和子文件夹，复制到路径destination处的文件夹。source和destination参数都是字符串。该函数返回一个字符串，是新复制的文件夹的路径。
'''
'''
#文件和文件夹的移动和改名
    调用shutil.move(spirce,destination),将路径source出的文件夹移动到路径destination，并返回新位置的绝对历经的字符串。
    如果destination指向一个文件夹，source文件将移动到destination中，并保持原来的文件名。
    使用move()时注意 这个move时移动并替换的意思 还能改名。
'''
'''
#永久删除文件和文件夹
    os模块可以删除一个文件或者一个空的文件夹，利用shutil可以删除一个文件夹及其所有内容
    调用shutil.rmtree(path)将删除path处的文件夹，它包含的所有文件和文件夹都会被删除。

    shutil.rmtree(path)函数和os模块的函数都是将文件彻底删除，可用send2trash作为删除文件的工具，这个删除是吧文件移动到垃圾桶
    #此模块为第三方模块 使用请pip install send2trash
    #send2trash.send2trash(path)
    
'''