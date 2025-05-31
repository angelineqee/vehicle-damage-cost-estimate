from flask import Flask, render_template, request, redirect, url_for,session
import os
from werkzeug.utils import secure_filename
from predict import detect_objects_in_image

image_path = './photos/sample.jpg'
model_path =  os.path.abspath(os.path.join('classifier','runs', 'detect', 'train9', 'weights', 'best.pt'))

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['OUTPUT_FOLDER'] = 'static/prediction_out'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}
app.secret_key = 'your_super_secret_key' 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def calculate_cost(part):
    if part=='Front':
        part_cost=500
        labor_cost=150
    elif part=='Rear':
        part_cost=400
        labor_cost=150
    elif part=='Side':
        part_cost=650
        labor_cost=200
    return {"part_cost":part_cost, "labor_cost":labor_cost,"total_cost":part_cost+labor_cost}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['selected_option'] = request.form.get('dropdown')
        file = request.files.get('file')

        if file and file.filename != '':
            # 🔥 Delete all files in the uploads folder first
            folder = app.config['UPLOAD_FOLDER']
            output_folder = app.config['OUTPUT_FOLDER']
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                if os.path.isfile(file_path):
                    os.remove(file_path)
            for filename in os.listdir(output_folder):
                file_path = os.path.join(output_folder, filename)
                if os.path.isfile(file_path):
                    os.remove(file_path)
            # Save new image
            filename = secure_filename(file.filename)
            file.save(os.path.join(folder, filename))
            output_img_path, results, highest_score = detect_objects_in_image(image_path=filename, model_path=model_path)
            if (results == None):
                session['image_url'] = filename
                session['damage']=False
            else:
                session['damage']=True
                session['image_url'] = output_img_path
                session['highest_score'] = highest_score
                session['costs']=calculate_cost(session['selected_option'])
        else:
            session['image_url'] = None

        return redirect(url_for('index'))

    selected_option = session.pop('selected_option', None)
    image_url = session.pop('image_url', None)
    damage = session.pop('damage', None)
    highest_score = session.pop('highest_score', None)
    costs = session.pop('costs', None)
    return render_template('index.html', damage=damage, selected_option=selected_option, image_url=image_url, highest_score=highest_score, costs=costs)

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
