"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9110 = "qa_fixture_token_9110_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9111 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9111)  # SQL injection candidate
OS_COMMAND_9112 = "convert " + user_supplied_path_9112  # command construction candidate
EXEC_RESULT_9113 = __import__("subprocess").run(OS_COMMAND_9113, shell=True)  # shell execution candidate
WEAK_DIGEST_9114 = __import__("hashlib").md5(payload_9114.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9115 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9116 = __import__("pickle").loads(serialized_payload_9116)  # unsafe deserialization candidate
YAML_OBJECT_9117 = __import__("yaml").load(yaml_text_9117, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9118 = "/srv/data/" + request_path_9118  # path traversal candidate
assert supplied_value_9119 == expected_value_9119  # assertion used for input validation candidate
