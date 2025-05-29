output "lambda_function_name" {
  description = "Name of the deployed Lambda function"
  value       = aws_lambda_function.spotify_lambda.function_name
}

output "lambda_function_arn" {
  description = "ARN of the deployed Lambda function"
  value       = aws_lambda_function.spotify_lambda.arn
}

output "eventbridge_rule_name" {
  description = "Name of the CloudWatch EventBridge rule"
  value       = aws_cloudwatch_event_rule.every_day.name
}
