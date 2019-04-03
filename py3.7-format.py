//python 3.7 feature 

library = [('Author', 'Topic', 'Pages'),('Twain', 'Rafting in water alone', 601),('Feynman', 'Physis', 95),('Hamilton', 'Mythology', 144)]

for author,topic,pages in library:
  print(f"{author:{10}} {topic:{30}} {pages:.>{10}}")
