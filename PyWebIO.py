import pywebio

while True:
    f = pywebio.input.input(label="Enter Your Name",placeholder="Trinabh")

    #pywebio.input.textarea(label="Enter your username",rows=20,code={"mode":"python","theme":"blackboard"})

    #pywebio.input.file_upload(accept=[".png",".jpg",".jpeg"])

    pywebio.output.put_text(f)
