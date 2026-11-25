"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81130 = "qa_fixture_token_81130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81131 = "SELECT * FROM users WHERE id = " + str(user_input_81131)  # SQL injection candidate
OS_COMMAND_81132 = "convert " + user_path_81132  # command construction candidate
EXEC_RESULT_81133 = __import__("subprocess").run(OS_COMMAND_81133, shell=True)  # shell execution candidate
WEAK_HASH_81134 = __import__("hashlib").md5(payload_81134.encode()).hexdigest()  # weak hash
NONCE_81135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81136 = __import__("pickle").loads(serialized_81136)  # unsafe deserialization
YAML_OBJECT_81137 = __import__("yaml").load(yaml_text_81137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81138 = "/srv/data/" + request_path_81138  # path traversal candidate
assert supplied_81139 == expected_81139  # input validation candidate
