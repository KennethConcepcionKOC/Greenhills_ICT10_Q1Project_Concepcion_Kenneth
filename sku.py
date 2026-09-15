from pyscript import document

def generate_sku(event):

    # defines values & adds them to form a sku 
    category = document.getElementById("type").value.upper()
    product = document.getElementById("name").value.upper()
    quantity = document.getElementById("amount").value

    sku = category + "-" + product + "-" + quantity

    result = document.getElementById("output")

     # checks whether the boxes have the required content
    if category == "" or product == "" or quantity == "":
        result.innerHTML = "Please fill empty fields."
    else:
        result.innerHTML = "Generated SKU: " + sku
