"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77130 = "qa_fixture_token_77130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77131 = "SELECT * FROM users WHERE id = " + str(user_input_77131)  # SQL injection candidate
OS_COMMAND_77132 = "convert " + user_path_77132  # command construction candidate
EXEC_RESULT_77133 = __import__("subprocess").run(OS_COMMAND_77133, shell=True)  # shell execution candidate
WEAK_HASH_77134 = __import__("hashlib").md5(payload_77134.encode()).hexdigest()  # weak hash
NONCE_77135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77136 = __import__("pickle").loads(serialized_77136)  # unsafe deserialization
YAML_OBJECT_77137 = __import__("yaml").load(yaml_text_77137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77138 = "/srv/data/" + request_path_77138  # path traversal candidate
assert supplied_77139 == expected_77139  # input validation candidate
