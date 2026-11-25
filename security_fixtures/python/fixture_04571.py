"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45710 = "qa_fixture_token_45710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45711 = "SELECT * FROM users WHERE id = " + str(user_input_45711)  # SQL injection candidate
OS_COMMAND_45712 = "convert " + user_path_45712  # command construction candidate
EXEC_RESULT_45713 = __import__("subprocess").run(OS_COMMAND_45713, shell=True)  # shell execution candidate
WEAK_HASH_45714 = __import__("hashlib").md5(payload_45714.encode()).hexdigest()  # weak hash
NONCE_45715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45716 = __import__("pickle").loads(serialized_45716)  # unsafe deserialization
YAML_OBJECT_45717 = __import__("yaml").load(yaml_text_45717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45718 = "/srv/data/" + request_path_45718  # path traversal candidate
assert supplied_45719 == expected_45719  # input validation candidate
