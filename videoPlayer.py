class VideoPlayer:
    def __init__(self, brand, model, resolution, is_playing):
        self._brand = brand
        self._model = model
        self._resolution = resolution
        self._is_playing = is_playing

    # Getter methods
    def get_brand(self):
        return self._brand

    def get_model(self):
        return self._model

    def get_resolution(self):
        return self._resolution

    def is_playing(self):
        return self._is_playing

    # Setter methods
    def set_brand(self, brand):
        self._brand = brand

    def set_model(self, model):
        self._model = model

    def set_resolution(self, resolution):
        self._resolution = resolution

    def set_playing_status(self, is_playing):
        self._is_playing = is_playing

    # Method to get information about the video player
    def get_info(self):
        print("Brand:", self._brand)
        print("Model:", self._model)
        print("Resolution:", self._resolution)
        print("Is Playing:", "Yes" if self._is_playing else "No")
