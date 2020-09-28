Project goal 
Create a dictionary with words and word frequencies that can be passed to the generate_from_frequencies function of the WordCloud class.

Once you have the dictionary, use this code to generate the word cloud image:
'''
cloud = wordcloud.WordCloud()
cloud.generate_from_frequencies(frequencies)
cloud.to_file("myfile.jpg")
'''
Things to remember 
1- Before processing any text, you need to remove all the punctuation marks. 
2- split a line of text into words.
3- Before storing words in the frequency dictionary, 
  check if they�re part of the "uninteresting" set of words 
  (for example: "a", "the", "to", "if"). 
  Make this set a parameter to your function so that you can change it if necessary.