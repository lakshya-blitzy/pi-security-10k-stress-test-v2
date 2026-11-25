"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_710 = "qa_fixture_token_710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_711 = "SELECT * FROM users WHERE id = " + str(user_input_711)  # SQL injection candidate
OS_COMMAND_712 = "convert " + user_path_712  # command construction candidate
EXEC_RESULT_713 = __import__("subprocess").run(OS_COMMAND_713, shell=True)  # shell execution candidate
WEAK_HASH_714 = __import__("hashlib").md5(payload_714.encode()).hexdigest()  # weak hash
NONCE_715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_716 = __import__("pickle").loads(serialized_716)  # unsafe deserialization
YAML_OBJECT_717 = __import__("yaml").load(yaml_text_717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_718 = "/srv/data/" + request_path_718  # path traversal candidate
assert supplied_719 == expected_719  # input validation candidate
