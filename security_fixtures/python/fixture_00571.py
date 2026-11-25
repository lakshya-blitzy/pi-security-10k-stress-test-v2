"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5710 = "qa_fixture_token_5710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5711 = "SELECT * FROM users WHERE id = " + str(user_input_5711)  # SQL injection candidate
OS_COMMAND_5712 = "convert " + user_path_5712  # command construction candidate
EXEC_RESULT_5713 = __import__("subprocess").run(OS_COMMAND_5713, shell=True)  # shell execution candidate
WEAK_HASH_5714 = __import__("hashlib").md5(payload_5714.encode()).hexdigest()  # weak hash
NONCE_5715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5716 = __import__("pickle").loads(serialized_5716)  # unsafe deserialization
YAML_OBJECT_5717 = __import__("yaml").load(yaml_text_5717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5718 = "/srv/data/" + request_path_5718  # path traversal candidate
assert supplied_5719 == expected_5719  # input validation candidate
