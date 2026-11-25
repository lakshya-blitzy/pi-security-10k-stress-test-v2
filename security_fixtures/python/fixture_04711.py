"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47110 = "qa_fixture_token_47110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47111 = "SELECT * FROM users WHERE id = " + str(user_input_47111)  # SQL injection candidate
OS_COMMAND_47112 = "convert " + user_path_47112  # command construction candidate
EXEC_RESULT_47113 = __import__("subprocess").run(OS_COMMAND_47113, shell=True)  # shell execution candidate
WEAK_HASH_47114 = __import__("hashlib").md5(payload_47114.encode()).hexdigest()  # weak hash
NONCE_47115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47116 = __import__("pickle").loads(serialized_47116)  # unsafe deserialization
YAML_OBJECT_47117 = __import__("yaml").load(yaml_text_47117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47118 = "/srv/data/" + request_path_47118  # path traversal candidate
assert supplied_47119 == expected_47119  # input validation candidate
