"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15130 = "qa_fixture_token_15130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15131 = "SELECT * FROM users WHERE id = " + str(user_input_15131)  # SQL injection candidate
OS_COMMAND_15132 = "convert " + user_path_15132  # command construction candidate
EXEC_RESULT_15133 = __import__("subprocess").run(OS_COMMAND_15133, shell=True)  # shell execution candidate
WEAK_HASH_15134 = __import__("hashlib").md5(payload_15134.encode()).hexdigest()  # weak hash
NONCE_15135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15136 = __import__("pickle").loads(serialized_15136)  # unsafe deserialization
YAML_OBJECT_15137 = __import__("yaml").load(yaml_text_15137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15138 = "/srv/data/" + request_path_15138  # path traversal candidate
assert supplied_15139 == expected_15139  # input validation candidate
