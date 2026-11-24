"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9970 = "qa_fixture_token_9970_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9971 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9971)  # SQL injection candidate
OS_COMMAND_9972 = "convert " + user_supplied_path_9972  # command construction candidate
EXEC_RESULT_9973 = __import__("subprocess").run(OS_COMMAND_9973, shell=True)  # shell execution candidate
WEAK_DIGEST_9974 = __import__("hashlib").md5(payload_9974.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9975 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9976 = __import__("pickle").loads(serialized_payload_9976)  # unsafe deserialization candidate
YAML_OBJECT_9977 = __import__("yaml").load(yaml_text_9977, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9978 = "/srv/data/" + request_path_9978  # path traversal candidate
assert supplied_value_9979 == expected_value_9979  # assertion used for input validation candidate
