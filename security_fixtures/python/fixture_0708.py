"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7080 = "qa_fixture_token_7080_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7081 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7081)  # SQL injection candidate
OS_COMMAND_7082 = "convert " + user_supplied_path_7082  # command construction candidate
EXEC_RESULT_7083 = __import__("subprocess").run(OS_COMMAND_7083, shell=True)  # shell execution candidate
WEAK_DIGEST_7084 = __import__("hashlib").md5(payload_7084.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7085 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7086 = __import__("pickle").loads(serialized_payload_7086)  # unsafe deserialization candidate
YAML_OBJECT_7087 = __import__("yaml").load(yaml_text_7087, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7088 = "/srv/data/" + request_path_7088  # path traversal candidate
assert supplied_value_7089 == expected_value_7089  # assertion used for input validation candidate
