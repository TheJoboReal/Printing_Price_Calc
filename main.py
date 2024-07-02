from appJar import gui
app = gui("Price Calculator", "600x400")

app.addLabel("title", "3D printing Price Calculator")
app.setLabelBg("title", "grey")

class Material:
    def __init__(self, price_pr_gram, price_pr_hour):
        self.price_pr_gram = price_pr_gram
        self.price_pr_hour = price_pr_hour

PLA = Material(0.23, 0.28)
TPU = Material(0.36, 0.34)

app.addLabelOptionBox("Material Type", ["PLA", "TPU"])
app.addLabelEntry("Material Used [g]")
app.addLabelEntry("Print Time")
app.addLabelEntry("Hours Used")
app.addCheckBox("Profit")
price = 0
app.addLabel("Total Price: ")

app.setBg("orange")
app.setFont(20)


def press(button):
    if button == "Cancel":
        app.stop()
    else:
        material_type = app.getOptionBox("Material Type")
        material_used = app.getEntry("Material Used [g]")
        print_time = app.getEntry("Print Time")

        # print("Material Type:", material_type)
        # print("Material Used [g]", material_used)
        # print("Print Time", print_time)

        if app.getCheckBox("Profit"):
            wage = float(app.getEntry("Hours Used"))
        else:
            wage = 0.0

        match material_type:
            case "PLA":
                price = float(material_used) * PLA.price_pr_gram + float(print_time) * PLA.price_pr_hour + wage * 200
            case "TPU":
                price = float(material_used) * TPU.price_pr_gram + float(print_time) * TPU.price_pr_hour + wage * 200
        
        # print("Total Price:", price)
        app.setLabel("Total Price: ", "Total Price: {:.3f}kr".format(price))

app.addButtons(["Calculate", "Cancel"], press)

app.go()