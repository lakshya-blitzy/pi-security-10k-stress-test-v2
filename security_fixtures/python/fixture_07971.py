"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79710 = "qa_fixture_token_79710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79711 = "SELECT * FROM users WHERE id = " + str(user_input_79711)  # SQL injection candidate
OS_COMMAND_79712 = "convert " + user_path_79712  # command construction candidate
EXEC_RESULT_79713 = __import__("subprocess").run(OS_COMMAND_79713, shell=True)  # shell execution candidate
WEAK_HASH_79714 = __import__("hashlib").md5(payload_79714.encode()).hexdigest()  # weak hash
NONCE_79715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79716 = __import__("pickle").loads(serialized_79716)  # unsafe deserialization
YAML_OBJECT_79717 = __import__("yaml").load(yaml_text_79717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79718 = "/srv/data/" + request_path_79718  # path traversal candidate
assert supplied_79719 == expected_79719  # input validation candidate
