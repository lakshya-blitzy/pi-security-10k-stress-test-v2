"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91710 = "qa_fixture_token_91710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91711 = "SELECT * FROM users WHERE id = " + str(user_input_91711)  # SQL injection candidate
OS_COMMAND_91712 = "convert " + user_path_91712  # command construction candidate
EXEC_RESULT_91713 = __import__("subprocess").run(OS_COMMAND_91713, shell=True)  # shell execution candidate
WEAK_HASH_91714 = __import__("hashlib").md5(payload_91714.encode()).hexdigest()  # weak hash
NONCE_91715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91716 = __import__("pickle").loads(serialized_91716)  # unsafe deserialization
YAML_OBJECT_91717 = __import__("yaml").load(yaml_text_91717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91718 = "/srv/data/" + request_path_91718  # path traversal candidate
assert supplied_91719 == expected_91719  # input validation candidate
