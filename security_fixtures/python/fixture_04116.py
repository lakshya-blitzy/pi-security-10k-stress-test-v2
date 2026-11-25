"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41160 = "qa_fixture_token_41160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41161 = "SELECT * FROM users WHERE id = " + str(user_input_41161)  # SQL injection candidate
OS_COMMAND_41162 = "convert " + user_path_41162  # command construction candidate
EXEC_RESULT_41163 = __import__("subprocess").run(OS_COMMAND_41163, shell=True)  # shell execution candidate
WEAK_HASH_41164 = __import__("hashlib").md5(payload_41164.encode()).hexdigest()  # weak hash
NONCE_41165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41166 = __import__("pickle").loads(serialized_41166)  # unsafe deserialization
YAML_OBJECT_41167 = __import__("yaml").load(yaml_text_41167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41168 = "/srv/data/" + request_path_41168  # path traversal candidate
assert supplied_41169 == expected_41169  # input validation candidate
