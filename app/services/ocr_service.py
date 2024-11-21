from PIL import Image
import pillow_heif
import io

def process_image(file):
    if file.filename.endswith(".heic"):
        heif_file = pillow_heif.read_heif(file.file)
        image = Image.frombytes(
            heif_file.mode, heif_file.size, heif_file.data, "raw", heif_file.mode
        )
        output = io.BytesIO()
        image.save(output, format="JPEG")
        output.seek(0)
        return output
    else:
        return file.file
    
def get_analytics_data(receipts_collection):
    """Fetch aggregated analytics data from MongoDB."""
    data = list(receipts_collection.find({}, {"_id": 0, "date": 1, "total": 1}))
    return data
