"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9500 = "qa_fixture_token_9500_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9501 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9501)  # SQL injection candidate
OS_COMMAND_9502 = "convert " + user_supplied_path_9502  # command construction candidate
EXEC_RESULT_9503 = __import__("subprocess").run(OS_COMMAND_9503, shell=True)  # shell execution candidate
WEAK_DIGEST_9504 = __import__("hashlib").md5(payload_9504.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9505 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9506 = __import__("pickle").loads(serialized_payload_9506)  # unsafe deserialization candidate
YAML_OBJECT_9507 = __import__("yaml").load(yaml_text_9507, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9508 = "/srv/data/" + request_path_9508  # path traversal candidate
assert supplied_value_9509 == expected_value_9509  # assertion used for input validation candidate
