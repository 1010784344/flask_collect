from flask import Flask, jsonify, render_template

app =  Flask(__name__)

# 存储进度数据
progress_mydata={}

@app.route('/')
def index():
    '''
    展示主页面
    '''
    return render_template('download.html')

@app.route('/progress_data/<uuid>')
def progress_data(uuid):
    '''
    通过uuid将数据存入变量progress_data
    '''
    for i in range(12345666):
        num_progress = round(i * 100 / 12345665, 2)

        progress_mydata[uuid] = num_progress
    return jsonify({'res': num_progress})

@app.route('/show_progress/<uuid>')
def show_progress(uuid):
    '''
    前端请求进度的函数
    '''
    return jsonify({'res': progress_mydata[uuid]})

if __name__ == '__main__':

    app.run(host='127.0.0.1', port=8013, debug=True)
