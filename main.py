import jinja2
import pdfkit
from datetime import datetime
import pywhatkit as kit
from html2image import Html2Image


def generate_img(context):
    template_loader = jinja2.FileSystemLoader('./')
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template("template.html")
    output_text = template.render(context)
    htmlimg = Html2Image()
    htmlimg.output_path = "images"
    filesize = (900, 800)
    htmlimg.screenshot(
        html_str=output_text,
        save_as="my_image.png",
        css_str="body{background-color:white!important;}",
        size=filesize
    )


def generate_pdf(contexts):
    template_loader = jinja2.FileSystemLoader('./')
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template("template.html")
    output_text = template.render(contexts)
    config = pdfkit.configuration(
        wkhtmltopdf=r"D:\User Data\Desktop\nishant\Projects\challan maker\wkhtmltopdf\bin\wkhtmltopdf.exe")
    pdfkit.from_string(output_text, "pdf_generated.pdf", configuration=config)


def send(number):
    caption = "Challan"
    kit.sendwhats_image(number, "images\my_image.png", caption)



c_no = int(input("Enter the Challan No.: "))
name = input("Enter the Name: ")
address = input("Enter the Address: ")
date = datetime.today().strftime("%d, %b, %y")
ph_no = input("Enter the Phone Number: ")
items = int(input("Enter the number of items: "))

context = {"challan_no": c_no, "name": name, "address": address, "phone_number": ph_no, "date": date}
for i in range(items):
    context["N" + str(i + 1)] = i + 1
    print("DETAILS OF ITEM-" + str(i + 1))
    context["D" + str(i + 1)] = input("Write the description of Item: ")
    context["R" + str(i + 1)] = int(input("Enter the rate of Item: "))
    context["A" + str(i + 1)] = int(input("Enter the amount of Item: "))

generate_img(context)

send("+91"+ph_no)
