# Spotify Playlist Automation with AWS Lambda & Terraform

This project automates the process of updating a Spotify playlist using AWS Lambda, EventBridge, and the Spotify API. It allows you to schedule daily updates to your playlist with a predefined list of tracks.

---

## Project Structure

```
terraform-spotify-lambda/
├── lambda/                      # Contains the Lambda function code
│   └── main.py                 # Python script to update Spotify playlist
├── terraform/                  # Terraform configurations
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── terraform.tfvars        # Stores your sensitive variables (not pushed to GitHub!)
├── get_refresh_token.py        # Script to generate Spotify refresh token
├── requirements.txt            # Python packages for Lambda function
├── lambda_package.zip          # Deployment package for Lambda (auto-generated)
└── README.md
```

---

## Step-by-Step Setup

### 1. Create a Spotify Developer App

- Go to: https://developer.spotify.com/dashboard
- Create a new app
- Get your:
  - Client ID
  - Client Secret

### 2. Set Redirect URIs

In your Spotify app, set this redirect URI:
```
http://localhost:8888/callback
```

### 3. Generate Refresh Token

Use the helper script:
```bash
python get_refresh_token.py
```

This will give you a refresh token used by the Lambda function.

---

## 4. Define Your Playlist

Go to your Spotify playlist and get the playlist ID from the URL:

Example:
```
https://open.spotify.com/playlist/00000000000000000
```
Playlist ID = `000000000000000`

---

## 5. Create terraform.tfvars

```hcl
aws_region            = "eu-west-1"
spotify_client_id     = "your-client-id"
spotify_client_secret = "your-client-secret"
spotify_refresh_token = "your-refresh-token"
spotify_playlist_id   = "your-playlist-id"
```

---

## 6. Build Lambda Deployment Package

```bash
pip install -r requirements.txt -t lambda/
cd lambda
zip -r9 ../lambda_package.zip .
cd ..
```

---

## 7. Deploy with Terraform

```bash
cd terraform
terraform init
terraform apply
```

---

## How It Works

- Lambda gets an access token from Spotify using the refresh token
- Adds predefined song URIs to the playlist
- Triggered daily by EventBridge

---

## Customizing the Song List

Edit the following section in `main.py`:

```python
"uris": [
    "spotify:track:3n3Ppam7vgaVa1iaRUc9Lp",
    "spotify:track:7ouMYWpwJ422jRcDASZB7P"
]
```

To convert Spotify links to URIs:  
https://developer.spotify.com/console/post-playlist-tracks/

---

## .gitignore

__pycache__/
*.py[cod]
*.so

# Environment variables
.env

# Lambda build artifacts
lambda/__pycache__/
lambda/*.dist-info/
lambda/*.egg-info/
lambda/requests/
lambda/urllib3/
lambda/chardet/
lambda/idna/
lambda/certifi/
lambda_package.zip

# OS files
.DS_Store
Thumbs.db

# Terraform
terraform/.terraform/
terraform/terraform.tfstate*
terraform/terraform.tfvars


# Zip packages
*.zip

get_refresh_token.py

---

## Final Note

This project was built to explore serverless automation and cloud-native workflows.  
Feel free to fork it, improve it, or use it as a base for your own Spotify integrations.

