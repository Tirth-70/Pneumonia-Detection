import os
import numpy as np
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import pickle
from flask_session import Session
from PIL import Image 



app = Flask(__name__)
app.config['SECRET_KEY'] = '123'  # Replace with a secure key
app.config['UPLOAD_FOLDER'] = 'static/uploads'  # Folder to store uploaded images
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

filename = 'best_model.pkl' 
model = pickle.load(open(filename, 'rb'))  # Replace with your model path

# return pass
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ['jpg', 'jpeg', 'png']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    if 'image' not in request.files:
        flash('No image uploaded!', 'error')
        return redirect(url_for('home'))
    flash('Processing image...', 'info')
    image_file = request.files['image']
    filename = secure_filename(image_file.filename)
    final_filename = "image."+filename.split(".")[-1]

    image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], final_filename))
    
    if image_file and allowed_file(final_filename):
        
        try:
            # Image preprocessing
            img_data = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], final_filename)).convert('RGB').resize((224, 224))
            image_array = np.array(img_data)
            image_array = image_array / 255.0  # Normalize pixel values
            image_batch = np.expand_dims(image_array, axis=0)  # Add batch dimension

            # Make prediction using your model
            prediction_probabilities = model.predict(image_batch)[0]
            class_names = ['Normal', 'Pneumonia']  # Assuming binary classification
            flash('Image processed!', 'success')

            # Display the prediction on the results page
            return render_template(
                'index.html',
                filename_display=filename,
                filename=final_filename,
                prediction=prediction_probabilities,
                class_names=class_names[0 if prediction_probabilities[0] < 0.5 else 1],
                normal_proba=100-(prediction_probabilities[0] * 100),
                pneumonia_proba=prediction_probabilities[0] * 100,
            )
        except Exception as e:
            flash(f'An error occurred: {e}', 'error')
            return redirect(url_for('home'))

    else:
        flash('Invalid image format. Please upload JPEG or PNG.', 'error')
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)  # Set debug=False for production