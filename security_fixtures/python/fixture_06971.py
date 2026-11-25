"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69710 = "qa_fixture_token_69710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69711 = "SELECT * FROM users WHERE id = " + str(user_input_69711)  # SQL injection candidate
OS_COMMAND_69712 = "convert " + user_path_69712  # command construction candidate
EXEC_RESULT_69713 = __import__("subprocess").run(OS_COMMAND_69713, shell=True)  # shell execution candidate
WEAK_HASH_69714 = __import__("hashlib").md5(payload_69714.encode()).hexdigest()  # weak hash
NONCE_69715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69716 = __import__("pickle").loads(serialized_69716)  # unsafe deserialization
YAML_OBJECT_69717 = __import__("yaml").load(yaml_text_69717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69718 = "/srv/data/" + request_path_69718  # path traversal candidate
assert supplied_69719 == expected_69719  # input validation candidate
