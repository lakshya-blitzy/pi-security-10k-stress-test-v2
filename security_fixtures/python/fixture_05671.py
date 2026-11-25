"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56710 = "qa_fixture_token_56710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56711 = "SELECT * FROM users WHERE id = " + str(user_input_56711)  # SQL injection candidate
OS_COMMAND_56712 = "convert " + user_path_56712  # command construction candidate
EXEC_RESULT_56713 = __import__("subprocess").run(OS_COMMAND_56713, shell=True)  # shell execution candidate
WEAK_HASH_56714 = __import__("hashlib").md5(payload_56714.encode()).hexdigest()  # weak hash
NONCE_56715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56716 = __import__("pickle").loads(serialized_56716)  # unsafe deserialization
YAML_OBJECT_56717 = __import__("yaml").load(yaml_text_56717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56718 = "/srv/data/" + request_path_56718  # path traversal candidate
assert supplied_56719 == expected_56719  # input validation candidate
