from videoPlayer import VideoPlayer
class VCR(VideoPlayer):
    def __init__(self, brand, model, resolution, is_playing, tape_type, recording_time, has_remote_control):
        # Call the constructor of the parent class
        super().__init__(brand, model, resolution, is_playing)

        # Add three additional parameters specific to VCR
        self._tape_type = tape_type
        self._recording_time = recording_time
        self._has_remote_control = has_remote_control

    # Getter methods for additional parameters
    def get_tape_type(self):
        return self._tape_type

    def get_recording_time(self):
        return self._recording_time

    def has_remote_control(self):
        return self._has_remote_control

    # Setter methods for additional parameters
    def set_tape_type(self, tape_type):
        self._tape_type = tape_type

    def set_recording_time(self, recording_time):
        self._recording_time = recording_time

    def set_remote_control_status(self, has_remote_control):
        self._has_remote_control = has_remote_control

    # Override the get_info method to include additional information
    def get_info(self):
        # Call the get_info method of the parent class
        super().get_info()
        # Include additional information specific to VCR
        print("Tape Type:", self._tape_type)
        print("Recording Time:", self._recording_time)
        print("Has Remote Control:", "Yes" if self._has_remote_control else "No")
