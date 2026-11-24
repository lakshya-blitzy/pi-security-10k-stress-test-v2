"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6080 = "qa_fixture_token_6080_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6081 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6081)  # SQL injection candidate
OS_COMMAND_6082 = "convert " + user_supplied_path_6082  # command construction candidate
EXEC_RESULT_6083 = __import__("subprocess").run(OS_COMMAND_6083, shell=True)  # shell execution candidate
WEAK_DIGEST_6084 = __import__("hashlib").md5(payload_6084.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6085 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6086 = __import__("pickle").loads(serialized_payload_6086)  # unsafe deserialization candidate
YAML_OBJECT_6087 = __import__("yaml").load(yaml_text_6087, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6088 = "/srv/data/" + request_path_6088  # path traversal candidate
assert supplied_value_6089 == expected_value_6089  # assertion used for input validation candidate
