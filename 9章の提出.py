
import os
os.path.join("Users", "bob", "st.txt")


st = open ("st.txt", "w")
st.write("Hi from Python!")
st.close()


st = open=("st.txt", "w", encording="utf-8")
st.write=("Pythonからこんにちは！")
st.close()

with open("st.txt", "w") as f:
    f.write("Hi from Python!")

with opem("st.txt", "r", encording="utf-8") as f:
    print(f.read())


my_list = []

with open ("st.txt", "r") as f:
    my_list.append(f.read())

    print(my_list)

