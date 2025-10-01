import pickle
from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)


def predictoin(list):
    filename = 'model/predictor.pickel'

    with open(filename, 'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict([list])
    return pred_value

@app.route('/', methods=['POST', 'GET'])
def index():
    pred = 0
    if request.method == 'POST':
        ram = request.form['ram']
        weight = request.form['weight']
        company = request.form['company']
        typename = request.form['typename']
        opsys = request.form['opsys']
        cpuname = request.form['cpuname']
        gpuname = request.form['gpuname']
        touchscreen = request.form.getlist('touchscreen')
        ips = request.form.getlist('ips')

        feature_list = []
        feature_list.append(int(ram))
        feature_list.append(float(weight))
        feature_list.append(len(touchscreen))
        feature_list.append(len(ips))
        
        company_list = ['acer', 'apple', 'asus', 'dell', 'hp', 'lenovo', 'msi', 'other', 'toshiba']
        typename_list = ['2in1convertible', 'gaming', 'netbook', 'notebook', 'ultrabook', 'workstation']
        opsys_list = ['linux', 'mac', 'other', 'windows']
        cpu_list = ['amd', 'intelcorei3', 'intelcorei5', 'intelcorei7', 'other']
        gpu_list = ['amd', 'intel', 'nvidia']


        def traves(list, value):
            for item in list:
                if item == value:
                    feature_list.append(1)
                else:
                    feature_list.append(0)

        traves(company_list, company)
        traves(typename_list, typename)
        traves(opsys_list, opsys)
        traves(cpu_list, cpuname)
        traves(gpu_list, gpuname)
        
        pred = predictoin(feature_list)*302.26
        pred = np.round(pred[0], 2)
    
        
    return render_template('index.html', pred = pred)

if __name__ == '__main__':
    app.run(debug=True)

