import json
import boto3

# Initialize the DynamoDB client. It will automatically use the same region
# as the Lambda function.
dynamodb = boto3.resource('dynamodb')

# Reference the DynamoDB table by its name.
table = dynamodb.Table('cloud-resume-views')

def lambda_handler(event, context):
    """
    This function is triggered by an API Gateway request. It increments a
    visitor counter in a DynamoDB table and returns the new count.
    """
    try:
        # Attempt to get the item with the primary key 'id' = 'resume'.
        response = table.get_item(Key={'id': 'resume'})
        
        # Check if the 'Item' key exists in the response. If it does, a record was found.
        if 'Item' in response:
            # Get the current 'views' count. If 'views' doesn't exist, default to 0.
            views = response['Item'].get('views', 0)
        else:
            # If no item was found, this is the very first visitor. Initialize the count to 0.
            views = 0
            
        # Increment the view count by 1.
        new_views = views + 1
        
        # Update the item in the DynamoDB table with the new count.
        # This uses an UpdateExpression to handle the reserved keyword 'views'.
        table.update_item(
            Key={'id': 'resume'},
            UpdateExpression='SET #v = :val',  # Use a placeholder '#v' for the attribute name.
            ExpressionAttributeNames={
                '#v': 'views'  # Define that the placeholder '#v' maps to the actual attribute name 'views'.
            },
            ExpressionAttributeValues={
                ':val': new_views  # Define that the placeholder ':val' maps to the new count.
            }
        )
        
        # Return a successful HTTP 200 response.
        # Include the necessary CORS headers to allow your website to access this API.
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "https://muhammadarsalan.site",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "GET, OPTIONS"
            },
            "body": json.dumps({
                "views": str(new_views) # Return the new count as a string in the response body.
            })
        }
    except Exception as e:
        # If any error occurs in the 'try' block, it will be caught here.
        # Log the detailed error to CloudWatch for debugging.
        print(f"Error: {e}")
        
        # Return an HTTP 500 Internal Server Error response.
        # Also include CORS headers on the error response.
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "https://muhammadarsalan.site",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "GET, OPTIONS"
            },
            "body": json.dumps({"message": "An error occurred"})
        }