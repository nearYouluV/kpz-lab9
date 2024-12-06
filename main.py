from VCR import VideoPlayer, VCR

my_video_player = VideoPlayer(brand="Sony", model="XYZ", resolution="1080p", is_playing=False)

# Get information using getter methods
print("Current Information:")
my_video_player.get_info()

# Update information using setter methods
my_video_player.set_resolution("4K")
my_video_player.set_playing_status(True)

# Display updated information using the get_info method
print("\nUpdated Information:")
my_video_player.get_info()
print("-"*40)
# Create a VCR object
my_vcr = VCR(
    brand="Panasonic", model="VCR-123", resolution="480p", is_playing=False,
    tape_type="VHS", recording_time="6 hours", has_remote_control=True
)
my_vcr.get_info()
print("\nUpdated Information:")
# Update information using setter methods
my_vcr.set_resolution("720p")
my_vcr.set_playing_status(True)
my_vcr.set_remote_control_status(False)
# Display updated information using the overridden get_info method
my_vcr.get_info()
