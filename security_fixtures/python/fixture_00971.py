"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9710 = "qa_fixture_token_9710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9711 = "SELECT * FROM users WHERE id = " + str(user_input_9711)  # SQL injection candidate
OS_COMMAND_9712 = "convert " + user_path_9712  # command construction candidate
EXEC_RESULT_9713 = __import__("subprocess").run(OS_COMMAND_9713, shell=True)  # shell execution candidate
WEAK_HASH_9714 = __import__("hashlib").md5(payload_9714.encode()).hexdigest()  # weak hash
NONCE_9715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9716 = __import__("pickle").loads(serialized_9716)  # unsafe deserialization
YAML_OBJECT_9717 = __import__("yaml").load(yaml_text_9717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9718 = "/srv/data/" + request_path_9718  # path traversal candidate
assert supplied_9719 == expected_9719  # input validation candidate
