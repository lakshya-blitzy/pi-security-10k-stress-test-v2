"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8110 = "qa_fixture_token_8110_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8111 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8111)  # SQL injection candidate
OS_COMMAND_8112 = "convert " + user_supplied_path_8112  # command construction candidate
EXEC_RESULT_8113 = __import__("subprocess").run(OS_COMMAND_8113, shell=True)  # shell execution candidate
WEAK_DIGEST_8114 = __import__("hashlib").md5(payload_8114.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8115 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8116 = __import__("pickle").loads(serialized_payload_8116)  # unsafe deserialization candidate
YAML_OBJECT_8117 = __import__("yaml").load(yaml_text_8117, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8118 = "/srv/data/" + request_path_8118  # path traversal candidate
assert supplied_value_8119 == expected_value_8119  # assertion used for input validation candidate
