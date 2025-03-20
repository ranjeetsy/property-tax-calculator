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
    
    breakdown = {
        "Building Tax (A)": round(A, 2),
        "Land Tax (B)": round(B, 2),
        "Beggar Cess (C = (A+B) × 3%)": round(C, 2),
        "Library Cess (D = (A+B) × 6%)": round(D, 2),
        "Health Cess (E = (A+B) × 15%)": round(E, 2),
        "Water Supply (F)": F,
        "Street Light Maintenance (G)": G,
        "Total Property Tax": round(total_tax, 2)
    }
    
    return breakdown

@app.route("/", methods=["GET", "POST"])
def index():
    breakdown = None
    if request.method == "POST":
        try:
            area = float(request.form["area"])
            breakdown = calculate_property_tax(area)
        except ValueError:
            breakdown = {"Error": "Invalid input! Please enter a numeric value."}
    return render_template("index.html", breakdown=breakdown)

if __name__ == "__main__":
    app.run(debug=True)
