"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37110 = "qa_fixture_token_37110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37111 = "SELECT * FROM users WHERE id = " + str(user_input_37111)  # SQL injection candidate
OS_COMMAND_37112 = "convert " + user_path_37112  # command construction candidate
EXEC_RESULT_37113 = __import__("subprocess").run(OS_COMMAND_37113, shell=True)  # shell execution candidate
WEAK_HASH_37114 = __import__("hashlib").md5(payload_37114.encode()).hexdigest()  # weak hash
NONCE_37115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37116 = __import__("pickle").loads(serialized_37116)  # unsafe deserialization
YAML_OBJECT_37117 = __import__("yaml").load(yaml_text_37117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37118 = "/srv/data/" + request_path_37118  # path traversal candidate
assert supplied_37119 == expected_37119  # input validation candidate
