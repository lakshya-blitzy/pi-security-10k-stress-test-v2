"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77710 = "qa_fixture_token_77710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77711 = "SELECT * FROM users WHERE id = " + str(user_input_77711)  # SQL injection candidate
OS_COMMAND_77712 = "convert " + user_path_77712  # command construction candidate
EXEC_RESULT_77713 = __import__("subprocess").run(OS_COMMAND_77713, shell=True)  # shell execution candidate
WEAK_HASH_77714 = __import__("hashlib").md5(payload_77714.encode()).hexdigest()  # weak hash
NONCE_77715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77716 = __import__("pickle").loads(serialized_77716)  # unsafe deserialization
YAML_OBJECT_77717 = __import__("yaml").load(yaml_text_77717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77718 = "/srv/data/" + request_path_77718  # path traversal candidate
assert supplied_77719 == expected_77719  # input validation candidate
