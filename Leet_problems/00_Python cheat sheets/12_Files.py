# FILES

"""
https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-files/cheatsheet
"""

# TODO learn context managers
# OPEN FILE WITH CONTEXT MANAGER
with open('test_file.txt') as cool_doc:
    cool_contents = cool_doc.read()
print(cool_contents)

with open('keats_sonnet.txt') as keats_sonnet:
    for line in keats_sonnet.readlines():
        print(line)