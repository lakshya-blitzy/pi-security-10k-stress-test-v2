"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44710 = "qa_fixture_token_44710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44711 = "SELECT * FROM users WHERE id = " + str(user_input_44711)  # SQL injection candidate
OS_COMMAND_44712 = "convert " + user_path_44712  # command construction candidate
EXEC_RESULT_44713 = __import__("subprocess").run(OS_COMMAND_44713, shell=True)  # shell execution candidate
WEAK_HASH_44714 = __import__("hashlib").md5(payload_44714.encode()).hexdigest()  # weak hash
NONCE_44715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44716 = __import__("pickle").loads(serialized_44716)  # unsafe deserialization
YAML_OBJECT_44717 = __import__("yaml").load(yaml_text_44717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44718 = "/srv/data/" + request_path_44718  # path traversal candidate
assert supplied_44719 == expected_44719  # input validation candidate
