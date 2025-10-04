from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

text = """

# Python3 program to find maximum
# in arr[] of size n

# python function to find maximum
# in arr[] of size n


def largest(arr, n):

    # Initialize maximum element
    max = arr[0]

    # Traverse array elements from second
    # and compare every element with
    # current max
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max


# Driver Code
arr = [10, 324, 45, 90, 9808]
n = len(arr)
Ans = largest(arr, n)
print("Largest in given array ", Ans)

"""
splitter = RecursiveCharacterTextSplitter.from_language(
    language = Language.PYTHON,
    chunk_size= 300,
    chunk_overlap = 0,
)

chunks = splitter.split_text(text)

print(len(chunks))

print(chunks)