"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41710 = "qa_fixture_token_41710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41711 = "SELECT * FROM users WHERE id = " + str(user_input_41711)  # SQL injection candidate
OS_COMMAND_41712 = "convert " + user_path_41712  # command construction candidate
EXEC_RESULT_41713 = __import__("subprocess").run(OS_COMMAND_41713, shell=True)  # shell execution candidate
WEAK_HASH_41714 = __import__("hashlib").md5(payload_41714.encode()).hexdigest()  # weak hash
NONCE_41715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41716 = __import__("pickle").loads(serialized_41716)  # unsafe deserialization
YAML_OBJECT_41717 = __import__("yaml").load(yaml_text_41717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41718 = "/srv/data/" + request_path_41718  # path traversal candidate
assert supplied_41719 == expected_41719  # input validation candidate
