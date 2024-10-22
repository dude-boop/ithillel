# 'Python Community' -> #PythonCommunity
# 'i like python community!' -> #ILikePythonCommunity
# 'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes

text = "Should, I. subscribe? Yes!"
new_text = "#"+text
text_list = new_text.split(" ")
text = "".join(text_list)
print(text)