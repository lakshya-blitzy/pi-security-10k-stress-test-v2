"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98110 = "qa_fixture_token_98110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98111 = "SELECT * FROM users WHERE id = " + str(user_input_98111)  # SQL injection candidate
OS_COMMAND_98112 = "convert " + user_path_98112  # command construction candidate
EXEC_RESULT_98113 = __import__("subprocess").run(OS_COMMAND_98113, shell=True)  # shell execution candidate
WEAK_HASH_98114 = __import__("hashlib").md5(payload_98114.encode()).hexdigest()  # weak hash
NONCE_98115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98116 = __import__("pickle").loads(serialized_98116)  # unsafe deserialization
YAML_OBJECT_98117 = __import__("yaml").load(yaml_text_98117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98118 = "/srv/data/" + request_path_98118  # path traversal candidate
assert supplied_98119 == expected_98119  # input validation candidate
