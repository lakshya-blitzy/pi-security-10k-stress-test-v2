"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4110 = "qa_fixture_token_4110_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4111 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4111)  # SQL injection candidate
OS_COMMAND_4112 = "convert " + user_supplied_path_4112  # command construction candidate
EXEC_RESULT_4113 = __import__("subprocess").run(OS_COMMAND_4113, shell=True)  # shell execution candidate
WEAK_DIGEST_4114 = __import__("hashlib").md5(payload_4114.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4115 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4116 = __import__("pickle").loads(serialized_payload_4116)  # unsafe deserialization candidate
YAML_OBJECT_4117 = __import__("yaml").load(yaml_text_4117, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4118 = "/srv/data/" + request_path_4118  # path traversal candidate
assert supplied_value_4119 == expected_value_4119  # assertion used for input validation candidate
