import os
import json

from flask import Flask, render_template, request, make_response, Response
from werkzeug.utils import secure_filename
import config


app = Flask(__name__)

# http://127.0.0.1:5000/mydownload

@app.route('/mydownload', methods=['POST', 'GET'])
def mul_upload_com():
    all_rule = config.ALLRULE
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)  # 当前文件所在路径

        upload_path = os.path.join(basepath, r'static/uploads', secure_filename(f.filename))
        f.save(upload_path)
        RuleBaseId = request.form['ruleinfo']


        with open(upload_path, 'r') as f:
            fdata_dict = json.load(f)

        result_str = json.dumps(fdata_dict, ensure_ascii=False, indent=4)


        # 删除原始文件
        os.remove(upload_path)

        out_json_name = config.ALLRULE[RuleBaseId] + '.json'
        out_json_name = out_json_name.encode("utf-8").decode("latin1")

        # 调动 chrome 文件下载的核心
        try:
            response = make_response(Response(result_str, mimetype='text/xml'))
            response.headers["Content-Disposition"] = "attachment; filename=%s;" % out_json_name
            return response

        except Exception as e:
            return '请联系管理员！'
    return render_template('upload_com.html', all_rule=all_rule.items())


if __name__ == '__main__':
    app.run(debug=True)

