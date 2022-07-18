import pickle

MODEL_PATH = r"E:\Graduation Project\Backend\django_project\crop_recommendation\crop_recommendation_model.sav"


class CropSuggestionModel():
    def __init__(self):
        #
        self.model = pickle.load(open(MODEL_PATH, 'rb'))

    def predict(self, temperature, humidity, ph, rainfal=0):
        try:
            return self.model.predict_proba([[temperature, humidity, ph, rainfal]])
        except:
            print("Error in prediction process")
            return False

    def prediction_as_list(self, prediction):
        j = 0
        result = []
        for i in prediction[0]:
            result.append({
                "crop_name": self.model.classes_[j],
                "precentage": int(i * 100)
            })
            j += 1
        return result

# prediction_as_list( model , predict(model,27.35,55.99,7.13,148) )

