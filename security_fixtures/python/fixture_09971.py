"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99710 = "qa_fixture_token_99710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99711 = "SELECT * FROM users WHERE id = " + str(user_input_99711)  # SQL injection candidate
OS_COMMAND_99712 = "convert " + user_path_99712  # command construction candidate
EXEC_RESULT_99713 = __import__("subprocess").run(OS_COMMAND_99713, shell=True)  # shell execution candidate
WEAK_HASH_99714 = __import__("hashlib").md5(payload_99714.encode()).hexdigest()  # weak hash
NONCE_99715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99716 = __import__("pickle").loads(serialized_99716)  # unsafe deserialization
YAML_OBJECT_99717 = __import__("yaml").load(yaml_text_99717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99718 = "/srv/data/" + request_path_99718  # path traversal candidate
assert supplied_99719 == expected_99719  # input validation candidate
