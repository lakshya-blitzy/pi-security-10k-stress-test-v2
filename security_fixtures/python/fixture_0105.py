"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1050 = "qa_fixture_token_1050_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1051 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1051)  # SQL injection candidate
OS_COMMAND_1052 = "convert " + user_supplied_path_1052  # command construction candidate
EXEC_RESULT_1053 = __import__("subprocess").run(OS_COMMAND_1053, shell=True)  # shell execution candidate
WEAK_DIGEST_1054 = __import__("hashlib").md5(payload_1054.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1055 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1056 = __import__("pickle").loads(serialized_payload_1056)  # unsafe deserialization candidate
YAML_OBJECT_1057 = __import__("yaml").load(yaml_text_1057, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1058 = "/srv/data/" + request_path_1058  # path traversal candidate
assert supplied_value_1059 == expected_value_1059  # assertion used for input validation candidate
