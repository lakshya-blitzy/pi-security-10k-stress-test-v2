"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32710 = "qa_fixture_token_32710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32711 = "SELECT * FROM users WHERE id = " + str(user_input_32711)  # SQL injection candidate
OS_COMMAND_32712 = "convert " + user_path_32712  # command construction candidate
EXEC_RESULT_32713 = __import__("subprocess").run(OS_COMMAND_32713, shell=True)  # shell execution candidate
WEAK_HASH_32714 = __import__("hashlib").md5(payload_32714.encode()).hexdigest()  # weak hash
NONCE_32715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32716 = __import__("pickle").loads(serialized_32716)  # unsafe deserialization
YAML_OBJECT_32717 = __import__("yaml").load(yaml_text_32717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32718 = "/srv/data/" + request_path_32718  # path traversal candidate
assert supplied_32719 == expected_32719  # input validation candidate
