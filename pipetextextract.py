import boto3

def lambda_handler(event, context):
# Document
    s3BucketName = "pipetextextract"
    documentName = "IMGPipe3.jpg"
# Amazon Textract client
#    textract = boto3.client('textract')
# Call Amazon Textract
#    response = textract.detect_document_text(
#        Document={
#            'S3Object': {
#                'Bucket': s3BucketName,
#                'Name': documentName,
#            }
#    })
#print(response)
# Print detected text
#    for item in response["Blocks"]:
#        if item["BlockType"] == "LINE":
#          #  print ('\033[' +  item["Text"] + '\033')
#            print (item["Text"])

    rekognition = boto3.client('rekognition')

    # Detect text in S3 image
    response = rekognition.detect_text(Image={'S3Object': {'Bucket': s3BucketName, 'Name': documentName}})
    # Process text detection results
    text_detections = response['TextDetections']
    extracted_text = ""
    for text_detection in text_detections:
        extracted_text += f"Detected text: {text_detection['DetectedText']} ({text_detection['Confidence']:.2f}%)\n"

        # Print or log extracted text
    print(extracted_text)