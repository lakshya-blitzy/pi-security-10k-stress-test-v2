"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95110 = "qa_fixture_token_95110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95111 = "SELECT * FROM users WHERE id = " + str(user_input_95111)  # SQL injection candidate
OS_COMMAND_95112 = "convert " + user_path_95112  # command construction candidate
EXEC_RESULT_95113 = __import__("subprocess").run(OS_COMMAND_95113, shell=True)  # shell execution candidate
WEAK_HASH_95114 = __import__("hashlib").md5(payload_95114.encode()).hexdigest()  # weak hash
NONCE_95115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95116 = __import__("pickle").loads(serialized_95116)  # unsafe deserialization
YAML_OBJECT_95117 = __import__("yaml").load(yaml_text_95117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95118 = "/srv/data/" + request_path_95118  # path traversal candidate
assert supplied_95119 == expected_95119  # input validation candidate
