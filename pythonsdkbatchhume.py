from google.cloud import storage
from hume import HumeBatchClient
from hume.models.config import FaceConfig, ProsodyConfig



client = HumeBatchClient("y7wUAPHS6ihjAyZsZwp4AN8EZtTFtyIfGnKJR4nRwhwLprDa", timeout=100)
# urls = ["https://mega.nz/file/w1Z2kaZS#wxaOtDFnCaTZ4kfixep4Nsv84quFRYjx0ffYEHyw4Z0"]
configs = [FaceConfig(identify_faces=True), ProsodyConfig()]
files = ["/Users/jetlin/Desktop/CalHacks/humeai/HumeReactionsCompressed/HumeReactions1compress.mp4"]
job = client.submit_job([], configs, files=files)

print(job)
print("Running...")

job.await_complete(timeout=300)
job.download_predictions("predictions.json")
print("Predictions downloaded to predictions.json")

job.download_artifacts("artifacts.zip")
print("Artifacts downloaded to artifacts.zip")

predictions = job.get_predictions()
print(predictions)