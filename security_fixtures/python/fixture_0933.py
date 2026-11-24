"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9330 = "qa_fixture_token_9330_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9331 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9331)  # SQL injection candidate
OS_COMMAND_9332 = "convert " + user_supplied_path_9332  # command construction candidate
EXEC_RESULT_9333 = __import__("subprocess").run(OS_COMMAND_9333, shell=True)  # shell execution candidate
WEAK_DIGEST_9334 = __import__("hashlib").md5(payload_9334.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9335 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9336 = __import__("pickle").loads(serialized_payload_9336)  # unsafe deserialization candidate
YAML_OBJECT_9337 = __import__("yaml").load(yaml_text_9337, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9338 = "/srv/data/" + request_path_9338  # path traversal candidate
assert supplied_value_9339 == expected_value_9339  # assertion used for input validation candidate
