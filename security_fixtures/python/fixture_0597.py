"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5970 = "qa_fixture_token_5970_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5971 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5971)  # SQL injection candidate
OS_COMMAND_5972 = "convert " + user_supplied_path_5972  # command construction candidate
EXEC_RESULT_5973 = __import__("subprocess").run(OS_COMMAND_5973, shell=True)  # shell execution candidate
WEAK_DIGEST_5974 = __import__("hashlib").md5(payload_5974.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5975 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5976 = __import__("pickle").loads(serialized_payload_5976)  # unsafe deserialization candidate
YAML_OBJECT_5977 = __import__("yaml").load(yaml_text_5977, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5978 = "/srv/data/" + request_path_5978  # path traversal candidate
assert supplied_value_5979 == expected_value_5979  # assertion used for input validation candidate
