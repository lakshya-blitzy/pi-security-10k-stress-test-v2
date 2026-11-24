"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1970 = "qa_fixture_token_1970_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1971 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1971)  # SQL injection candidate
OS_COMMAND_1972 = "convert " + user_supplied_path_1972  # command construction candidate
EXEC_RESULT_1973 = __import__("subprocess").run(OS_COMMAND_1973, shell=True)  # shell execution candidate
WEAK_DIGEST_1974 = __import__("hashlib").md5(payload_1974.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1975 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1976 = __import__("pickle").loads(serialized_payload_1976)  # unsafe deserialization candidate
YAML_OBJECT_1977 = __import__("yaml").load(yaml_text_1977, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1978 = "/srv/data/" + request_path_1978  # path traversal candidate
assert supplied_value_1979 == expected_value_1979  # assertion used for input validation candidate
