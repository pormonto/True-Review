from hume import HumeBatchClient
from hume.models.config import FaceConfig
from pprint import pprint


# Provide the absolute path to the image file
image_path = "/Users/jetlin/Desktop/CalHacks/humeai/mossman.JPG"

# Use the absolute path in the urls list


client = HumeBatchClient("y7wUAPHS6ihjAyZsZwp4AN8EZtTFtyIfGnKJR4nRwhwLprDa")
# urls = [image_path]
urls = ["	https://iep.utm.edu/wp-content/media/Nietzsche.jpg"]
config = FaceConfig()
job = client.submit_job(urls, [config])

status = job.get_status()
print(f"Job status: {status}")

details = job.get_details()
run_time_ms = details.get_run_time_ms()
print(f"Job ran for {run_time_ms} milliseconds")




predictions = job.get_predictions()
pprint(predictions)