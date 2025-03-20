from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_property_tax(super_built_up_area):
    A = super_built_up_area * 2.12  # Building Tax
    B = super_built_up_area * 1.39  # Land Tax
    C = (A + B) * 0.03  # Beggar Cess (3%)
    D = (A + B) * 0.06  # Library Cess (6%)
    E = (A + B) * 0.15  # Health Cess (15%)
    F = 100  # Water Supply (Fixed)
    G = 100  # Street Light Maintenance (Fixed)
    
    total_tax = A + B + C + D + E + F + G
    return round(total_tax, 2)

@app.route("/", methods=["GET", "POST"])
def index():
    tax = None
    if request.method == "POST":
        try:
            area = float(request.form["area"])
            tax = calculate_property_tax(area)
        except ValueError:
            tax = "Invalid input! Please enter a numeric value."
    return render_template("index.html", tax=tax)

if __name__ == "__main__":
    app.run(debug=True)
