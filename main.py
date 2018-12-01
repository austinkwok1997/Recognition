import boto3

if __name__ == "__main__":

    imageFile='canucks2.jpg'
    client=boto3.client('rekognition')
   
    with open(imageFile, 'rb') as image:
        response = client.detect_faces(Image={'Bytes': image.read()})
        
    print('Detected labels in ' + imageFile)    
    # for label in response['Labels']:
    #     print (label['Name'] + ' : ' + str(label['Confidence']))
    print(len(response['FaceDetails']))

    print('Done...')