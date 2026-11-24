"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1060 = "qa_fixture_token_1060_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1061 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1061)  # SQL injection candidate
OS_COMMAND_1062 = "convert " + user_supplied_path_1062  # command construction candidate
EXEC_RESULT_1063 = __import__("subprocess").run(OS_COMMAND_1063, shell=True)  # shell execution candidate
WEAK_DIGEST_1064 = __import__("hashlib").md5(payload_1064.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1065 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1066 = __import__("pickle").loads(serialized_payload_1066)  # unsafe deserialization candidate
YAML_OBJECT_1067 = __import__("yaml").load(yaml_text_1067, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1068 = "/srv/data/" + request_path_1068  # path traversal candidate
assert supplied_value_1069 == expected_value_1069  # assertion used for input validation candidate
