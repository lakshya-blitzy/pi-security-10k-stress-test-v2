"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21130 = "qa_fixture_token_21130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21131 = "SELECT * FROM users WHERE id = " + str(user_input_21131)  # SQL injection candidate
OS_COMMAND_21132 = "convert " + user_path_21132  # command construction candidate
EXEC_RESULT_21133 = __import__("subprocess").run(OS_COMMAND_21133, shell=True)  # shell execution candidate
WEAK_HASH_21134 = __import__("hashlib").md5(payload_21134.encode()).hexdigest()  # weak hash
NONCE_21135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21136 = __import__("pickle").loads(serialized_21136)  # unsafe deserialization
YAML_OBJECT_21137 = __import__("yaml").load(yaml_text_21137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21138 = "/srv/data/" + request_path_21138  # path traversal candidate
assert supplied_21139 == expected_21139  # input validation candidate
