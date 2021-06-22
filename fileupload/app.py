

import os

from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import logging


app = Flask(__name__)

# 日志系统配置
# 日志器设置日志级别（日志器来自于 flask）
app.logger.setLevel(logging.DEBUG)

# 处理器（处理器来自于 logging 模块）
handler = logging.FileHandler('my.log', encoding='UTF-8')
logging_format = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
handler.setFormatter(logging_format)

# 日志器和处理器进行关联
app.logger.addHandler(handler)


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)  # 当前文件所在路径

        # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
        upload_path = os.path.join(basepath, r'static\uploads', secure_filename(f.filename))
        f.save(upload_path)
        # 文件上传成功添加日志信息
        # 方式一（可以在任何一个模块使用的）
        # from flask import current_app
        # current_app.logger.info('文件上传成功')
        # 方式二
        app.logger.info('info log')

        return redirect(url_for('upload'))
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)


