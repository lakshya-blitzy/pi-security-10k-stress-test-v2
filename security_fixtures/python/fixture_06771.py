"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67710 = "qa_fixture_token_67710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67711 = "SELECT * FROM users WHERE id = " + str(user_input_67711)  # SQL injection candidate
OS_COMMAND_67712 = "convert " + user_path_67712  # command construction candidate
EXEC_RESULT_67713 = __import__("subprocess").run(OS_COMMAND_67713, shell=True)  # shell execution candidate
WEAK_HASH_67714 = __import__("hashlib").md5(payload_67714.encode()).hexdigest()  # weak hash
NONCE_67715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67716 = __import__("pickle").loads(serialized_67716)  # unsafe deserialization
YAML_OBJECT_67717 = __import__("yaml").load(yaml_text_67717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67718 = "/srv/data/" + request_path_67718  # path traversal candidate
assert supplied_67719 == expected_67719  # input validation candidate
