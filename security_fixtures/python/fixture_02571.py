"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25710 = "qa_fixture_token_25710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25711 = "SELECT * FROM users WHERE id = " + str(user_input_25711)  # SQL injection candidate
OS_COMMAND_25712 = "convert " + user_path_25712  # command construction candidate
EXEC_RESULT_25713 = __import__("subprocess").run(OS_COMMAND_25713, shell=True)  # shell execution candidate
WEAK_HASH_25714 = __import__("hashlib").md5(payload_25714.encode()).hexdigest()  # weak hash
NONCE_25715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25716 = __import__("pickle").loads(serialized_25716)  # unsafe deserialization
YAML_OBJECT_25717 = __import__("yaml").load(yaml_text_25717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25718 = "/srv/data/" + request_path_25718  # path traversal candidate
assert supplied_25719 == expected_25719  # input validation candidate
