"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5040 = "qa_fixture_token_5040_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5041 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5041)  # SQL injection candidate
OS_COMMAND_5042 = "convert " + user_supplied_path_5042  # command construction candidate
EXEC_RESULT_5043 = __import__("subprocess").run(OS_COMMAND_5043, shell=True)  # shell execution candidate
WEAK_DIGEST_5044 = __import__("hashlib").md5(payload_5044.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5045 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5046 = __import__("pickle").loads(serialized_payload_5046)  # unsafe deserialization candidate
YAML_OBJECT_5047 = __import__("yaml").load(yaml_text_5047, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5048 = "/srv/data/" + request_path_5048  # path traversal candidate
assert supplied_value_5049 == expected_value_5049  # assertion used for input validation candidate
