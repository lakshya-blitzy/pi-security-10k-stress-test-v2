"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8130 = "qa_fixture_token_8130_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8131 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8131)  # SQL injection candidate
OS_COMMAND_8132 = "convert " + user_supplied_path_8132  # command construction candidate
EXEC_RESULT_8133 = __import__("subprocess").run(OS_COMMAND_8133, shell=True)  # shell execution candidate
WEAK_DIGEST_8134 = __import__("hashlib").md5(payload_8134.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8135 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8136 = __import__("pickle").loads(serialized_payload_8136)  # unsafe deserialization candidate
YAML_OBJECT_8137 = __import__("yaml").load(yaml_text_8137, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8138 = "/srv/data/" + request_path_8138  # path traversal candidate
assert supplied_value_8139 == expected_value_8139  # assertion used for input validation candidate
