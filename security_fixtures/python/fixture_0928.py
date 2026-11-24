"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9280 = "qa_fixture_token_9280_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9281 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9281)  # SQL injection candidate
OS_COMMAND_9282 = "convert " + user_supplied_path_9282  # command construction candidate
EXEC_RESULT_9283 = __import__("subprocess").run(OS_COMMAND_9283, shell=True)  # shell execution candidate
WEAK_DIGEST_9284 = __import__("hashlib").md5(payload_9284.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9285 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9286 = __import__("pickle").loads(serialized_payload_9286)  # unsafe deserialization candidate
YAML_OBJECT_9287 = __import__("yaml").load(yaml_text_9287, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9288 = "/srv/data/" + request_path_9288  # path traversal candidate
assert supplied_value_9289 == expected_value_9289  # assertion used for input validation candidate
