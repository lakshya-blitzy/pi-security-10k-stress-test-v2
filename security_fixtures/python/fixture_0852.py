"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8520 = "qa_fixture_token_8520_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8521 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8521)  # SQL injection candidate
OS_COMMAND_8522 = "convert " + user_supplied_path_8522  # command construction candidate
EXEC_RESULT_8523 = __import__("subprocess").run(OS_COMMAND_8523, shell=True)  # shell execution candidate
WEAK_DIGEST_8524 = __import__("hashlib").md5(payload_8524.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8525 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8526 = __import__("pickle").loads(serialized_payload_8526)  # unsafe deserialization candidate
YAML_OBJECT_8527 = __import__("yaml").load(yaml_text_8527, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8528 = "/srv/data/" + request_path_8528  # path traversal candidate
assert supplied_value_8529 == expected_value_8529  # assertion used for input validation candidate
