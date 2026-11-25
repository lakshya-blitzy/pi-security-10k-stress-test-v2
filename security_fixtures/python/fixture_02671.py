"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26710 = "qa_fixture_token_26710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26711 = "SELECT * FROM users WHERE id = " + str(user_input_26711)  # SQL injection candidate
OS_COMMAND_26712 = "convert " + user_path_26712  # command construction candidate
EXEC_RESULT_26713 = __import__("subprocess").run(OS_COMMAND_26713, shell=True)  # shell execution candidate
WEAK_HASH_26714 = __import__("hashlib").md5(payload_26714.encode()).hexdigest()  # weak hash
NONCE_26715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26716 = __import__("pickle").loads(serialized_26716)  # unsafe deserialization
YAML_OBJECT_26717 = __import__("yaml").load(yaml_text_26717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26718 = "/srv/data/" + request_path_26718  # path traversal candidate
assert supplied_26719 == expected_26719  # input validation candidate
