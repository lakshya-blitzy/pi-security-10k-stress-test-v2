"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9420 = "qa_fixture_token_9420_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9421 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9421)  # SQL injection candidate
OS_COMMAND_9422 = "convert " + user_supplied_path_9422  # command construction candidate
EXEC_RESULT_9423 = __import__("subprocess").run(OS_COMMAND_9423, shell=True)  # shell execution candidate
WEAK_DIGEST_9424 = __import__("hashlib").md5(payload_9424.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9425 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9426 = __import__("pickle").loads(serialized_payload_9426)  # unsafe deserialization candidate
YAML_OBJECT_9427 = __import__("yaml").load(yaml_text_9427, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9428 = "/srv/data/" + request_path_9428  # path traversal candidate
assert supplied_value_9429 == expected_value_9429  # assertion used for input validation candidate
