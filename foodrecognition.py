from all_imports import *


def preprocess_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (128, 128))
    image = image.astype(np.float32) / 255.0
    image = preprocess_input(image)
    image = np.expand_dims(image, axis=0)
    return image


def predict_with_vgg_model(image_path):
    vgg_model = load_model('vgg_model.h5')
    image = preprocess_image(image_path)
    prediction = vgg_model.predict(image)
    predicted_class = np.argmax(prediction)

    print("Predicted Class:", predicted_class)

    base_dir = 'static/LuxembourgFood'
    class_labels = sorted(os.listdir(base_dir))
    class_mapping = {i: class_label for i, class_label in enumerate(class_labels)}
    predicted_class_index = predicted_class
    predicted_class_label = class_mapping[predicted_class_index]

    print("Predicted Class Label:", predicted_class_label)

    return predicted_class_label
