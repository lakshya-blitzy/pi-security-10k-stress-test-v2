"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9080 = "qa_fixture_token_9080_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9081 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9081)  # SQL injection candidate
OS_COMMAND_9082 = "convert " + user_supplied_path_9082  # command construction candidate
EXEC_RESULT_9083 = __import__("subprocess").run(OS_COMMAND_9083, shell=True)  # shell execution candidate
WEAK_DIGEST_9084 = __import__("hashlib").md5(payload_9084.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9085 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9086 = __import__("pickle").loads(serialized_payload_9086)  # unsafe deserialization candidate
YAML_OBJECT_9087 = __import__("yaml").load(yaml_text_9087, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9088 = "/srv/data/" + request_path_9088  # path traversal candidate
assert supplied_value_9089 == expected_value_9089  # assertion used for input validation candidate
