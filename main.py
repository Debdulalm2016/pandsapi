#script: main.py
from flask import Flask, render_template, request, jsonify, url_for, redirect
import modulepg
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET', 'POST'])
def gdatapy_home():
    return "<h1>PANDSAPI HOME</h1><p>This is indication that App is active</p>"

@app.errorhandler(404)
def page_not_found(e):
	return "<h1>404</h1><p>The resource could not be found</p>", 404

    
@app.route("/api/v1/wbdistricts/json", methods=['GET'])
def api_json_wbdistricts():
    list_districts = modulepg.Get_WB_Districts()
    if(list_districts):
    	return jsonify(list_districts)
    else:
    	return jsonify([])

@app.route("/api/v1/wbsubdivsindistrict/json/<distname>", methods=['GET'])
def api_json_wbsubdivsindistrict(distname):
    list_subdivs = modulepg.Get_WB_Subdivs_in_District(distname)
    if(list_subdivs):
    	return jsonify(list_subdivs)
    else:
        return jsonify([])

@app.route("/api/v1/wbblocksinsubdiv/json/<subdivname>", methods=['GET'])
def api_json_wbblocksinsubdiv(subdivname):
    list_blocks = modulepg.Get_WB_Blocks_in_Subdiv(subdivname)
    if(list_blocks):
    	return jsonify(list_blocks)
    else:
        return jsonify([])

@app.route("/api/v1/wbgpsinblock/json/<blockname>", methods=['GET'])
def api_json_wbgpsinblock(blockname):
    list_gps = modulepg.Get_WB_GPs_in_Block(blockname)
    if(list_gps):
    	return jsonify(list_gps)
    else:
        return jsonify([])

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))


