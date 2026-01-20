"""
Docstring for 32.Title Consistency Checker: This program Checks if easy word it Titled or not.
    Cases;
            ✅ Consistent Title Case
               1. "The Quick Brown Fox"                     |
               2. "Data Science Fundamentals"               | ==> First letter Uppercase + rest lowercase
               3. "Python Programming Basics"               | 
               4. "Artificial Intelligence Revolution"                
               5. "Statistics For Beginners"                
            
            ❌ Not Consistent
               1. "the quick Brown fox" → first word lowercase                
               2. "Data science Fundamentals" → middle word not capitalized                
               3. "PYTHON programming Basics" → mixed casing                
               4. "Artificial intelligence revolution" → only first word capitalized                
               5. "Statistics for Beginners" → “for” lowercase (depends on strictness rules)
    
    Efficiency: Time complexity is O(n)
                Space complexity is O(1)
                Where n is the length of the string.


"""
phrase = input("Enter the sentence or Paragraph: ").split()

def title_check(k):
    for word in k:
        if word.capitalize() != word:
            return False
    return True

if title_check(phrase):
    print("The provided sentence is Consistently Titled")
else:
    print("The provided sentence has not been Titled")