from flask import Flask, render_template, request, jsonify
from utils import Sales_price_prediction

sales_pp = Sales_price_prediction()

app = Flask(__name__,template_folder='template')

@app.route('/')
def hello():
    print("hello flask")
    #return 'hello sanket'
    return render_template('index.html')

@app.route('/sales_price_predict', methods = ['POST','GET'])
def predict_sales_price():
    if request.method == "POST":
        user_data = request.form
        TV_sales = eval(user_data['TV_sales'])
        Radio_sales = eval(user_data['Radio_sales'])
        News_paper_sales = eval(user_data['News_paper_sales'])
        

        print('TV_sales', 'Radio_sales', 'News_paper_sales',TV_sales, Radio_sales,News_paper_sales)
        Sales_price = sales_pp.price_pred(TV_sales, Radio_sales, News_paper_sales)
        
        #return jsonify({"Message": f"Predicted sales price is {Sales_price} $"})
        return render_template('index.html',price_prediction=Sales_price)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5004)
        