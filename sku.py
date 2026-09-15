from pyscript import document

def generate_sku(event):

    category = document.getElementById("type").value.upper()
    product = document.getElementById("name").value.upper()
    quantity = document.getElementById("amount").value

    sku = category + "-" + product + "-" + quantity

    result = document.getElementById("output")

    if category == "" or product == "" or quantity == "":
        result.innerHTML = "Please fill empty fields."
    else:
        result.innerHTML = "Generated SKU: " + sku