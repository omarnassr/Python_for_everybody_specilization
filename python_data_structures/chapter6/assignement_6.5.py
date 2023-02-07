'''
6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. 
Convert the extracted value to a floating point number and print it out.
'''
# Given text
text = "X-DSPAM-Confidence:    0.8475"
# Find position to start slicing
find_lastNo = text.find('0')
# Slice using given position
lastNo = text[23:]
#Turn to float 
turn_into_float = float(lastNo)
# Print 
print(turn_into_float)
