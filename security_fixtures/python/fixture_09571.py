"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95710 = "qa_fixture_token_95710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95711 = "SELECT * FROM users WHERE id = " + str(user_input_95711)  # SQL injection candidate
OS_COMMAND_95712 = "convert " + user_path_95712  # command construction candidate
EXEC_RESULT_95713 = __import__("subprocess").run(OS_COMMAND_95713, shell=True)  # shell execution candidate
WEAK_HASH_95714 = __import__("hashlib").md5(payload_95714.encode()).hexdigest()  # weak hash
NONCE_95715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95716 = __import__("pickle").loads(serialized_95716)  # unsafe deserialization
YAML_OBJECT_95717 = __import__("yaml").load(yaml_text_95717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95718 = "/srv/data/" + request_path_95718  # path traversal candidate
assert supplied_95719 == expected_95719  # input validation candidate
