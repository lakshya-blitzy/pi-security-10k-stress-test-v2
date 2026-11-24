"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4970 = "qa_fixture_token_4970_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4971 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4971)  # SQL injection candidate
OS_COMMAND_4972 = "convert " + user_supplied_path_4972  # command construction candidate
EXEC_RESULT_4973 = __import__("subprocess").run(OS_COMMAND_4973, shell=True)  # shell execution candidate
WEAK_DIGEST_4974 = __import__("hashlib").md5(payload_4974.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4975 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4976 = __import__("pickle").loads(serialized_payload_4976)  # unsafe deserialization candidate
YAML_OBJECT_4977 = __import__("yaml").load(yaml_text_4977, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4978 = "/srv/data/" + request_path_4978  # path traversal candidate
assert supplied_value_4979 == expected_value_4979  # assertion used for input validation candidate
