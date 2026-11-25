"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64710 = "qa_fixture_token_64710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64711 = "SELECT * FROM users WHERE id = " + str(user_input_64711)  # SQL injection candidate
OS_COMMAND_64712 = "convert " + user_path_64712  # command construction candidate
EXEC_RESULT_64713 = __import__("subprocess").run(OS_COMMAND_64713, shell=True)  # shell execution candidate
WEAK_HASH_64714 = __import__("hashlib").md5(payload_64714.encode()).hexdigest()  # weak hash
NONCE_64715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64716 = __import__("pickle").loads(serialized_64716)  # unsafe deserialization
YAML_OBJECT_64717 = __import__("yaml").load(yaml_text_64717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64718 = "/srv/data/" + request_path_64718  # path traversal candidate
assert supplied_64719 == expected_64719  # input validation candidate
