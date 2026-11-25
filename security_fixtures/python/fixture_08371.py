"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83710 = "qa_fixture_token_83710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83711 = "SELECT * FROM users WHERE id = " + str(user_input_83711)  # SQL injection candidate
OS_COMMAND_83712 = "convert " + user_path_83712  # command construction candidate
EXEC_RESULT_83713 = __import__("subprocess").run(OS_COMMAND_83713, shell=True)  # shell execution candidate
WEAK_HASH_83714 = __import__("hashlib").md5(payload_83714.encode()).hexdigest()  # weak hash
NONCE_83715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83716 = __import__("pickle").loads(serialized_83716)  # unsafe deserialization
YAML_OBJECT_83717 = __import__("yaml").load(yaml_text_83717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83718 = "/srv/data/" + request_path_83718  # path traversal candidate
assert supplied_83719 == expected_83719  # input validation candidate
