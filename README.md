**Pneumonia Detection Web App**

This web app allows users to upload chest X-ray images and determines the likelihood of pneumonia using a trained deep learning model.

**Features**

*   Image upload (JPEG, PNG)
*   Real-time pneumonia prediction from uploaded X-rays
*   Probability estimates for both Normal and Pneumonia classes
*   Displays the uploaded image with the predicted class

**Technologies**

*   Python
*   Flask
*   TensorFlow/Keras
*   HTML/CSS
*   JavaScript (for basic image preview)

**How to Run Locally**

1.  **Clone the repository**

    ```bash
    git clone https://github.com/Tirth-70/Pneumonia-Detection.git
    ```

2.  **Install required packages:**

    ```bash
    cd Pneumonia-Detection
    pip install -r requirements.txt
    ```

3.  **Run the application:**

    ```bash
    python app.py
    ```

4.  **Open your web browser and navigate to:**

    ```
    http://localhost:8080 
    ```

**Directory Structure**

*   **static**
    *   `style.css`: Contains CSS styles for the web app.
    *   `uploads`: Stores uploaded images.
*   **templates**
    *   `index.html`:  Contains the HTML structure and form.
*   `app.py`:  Main Flask application file.
*   `requirements.txt`:  Lists required Python dependencies. 
*   `generator.ipynb`: (Presumably) Your training notebook, consider renaming it `train.ipynb` or similar if that's more accurate
*   `best_model1.h5`: (Presumably) Contains your best trained model.

**Model Training**

The `generator.ipynb` file (or a similarly named `train.ipynb`) presumably contains the code used to train the deep learning model. Details about the training dataset, preprocessing steps, and model architecture can be added to the README or included in a separate `training_notes.txt` file for more thorough documentation.

**Contributing**

[Feel free to suggest improvements or raise issues if you encounter any bugs.] (Replace with your own contribution guidelines, if desired).

**Disclaimer**

<<<<<<< HEAD
This project is intended for educational and demonstration purposes.  It is not a substitute for professional medical advice.
=======
This project is intended for educational and demonstration purposes.  It is not a substitute for professional medical advice.
>>>>>>> dbba9d4 (Updated README)
