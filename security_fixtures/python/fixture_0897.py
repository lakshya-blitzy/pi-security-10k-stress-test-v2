"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8970 = "qa_fixture_token_8970_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8971 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8971)  # SQL injection candidate
OS_COMMAND_8972 = "convert " + user_supplied_path_8972  # command construction candidate
EXEC_RESULT_8973 = __import__("subprocess").run(OS_COMMAND_8973, shell=True)  # shell execution candidate
WEAK_DIGEST_8974 = __import__("hashlib").md5(payload_8974.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8975 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8976 = __import__("pickle").loads(serialized_payload_8976)  # unsafe deserialization candidate
YAML_OBJECT_8977 = __import__("yaml").load(yaml_text_8977, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8978 = "/srv/data/" + request_path_8978  # path traversal candidate
assert supplied_value_8979 == expected_value_8979  # assertion used for input validation candidate
