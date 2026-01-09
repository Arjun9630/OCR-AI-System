import cv2

def preprocess_image(image_path: str):
    """
    OCR-optimized preprocessing for structured documents.
    """

    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Unable to read image from path: {image_path}")

    # Grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Upscale (2x)
    h, w = gray.shape
    upscaled = cv2.resize(
        gray,
        (w * 2, h * 2),
        interpolation=cv2.INTER_CUBIC
    )

    # Light denoising
    denoised = cv2.fastNlMeansDenoising(upscaled, h=10)

    # Contrast enhancement
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(denoised)

    return enhanced
