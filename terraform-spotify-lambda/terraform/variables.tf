variable "aws_region" {
  description = "AWS region to deploy resources in"
  type        = string
  default     = "eu-west-1" # You can change this if you're in a different region
}

variable "spotify_client_id" {
  description = "Your Spotify Developer Client ID"
  type        = string
  sensitive   = true
}

variable "spotify_client_secret" {
  description = "Your Spotify Developer Client Secret"
  type        = string
  sensitive   = true
}

variable "spotify_refresh_token" {
  description = "Refresh token to generate a valid access token for Spotify API"
  type        = string
  sensitive   = true
}

variable "spotify_playlist_id" {
  description = "The Spotify Playlist ID you want to update"
  type        = string
}
