"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12710 = "qa_fixture_token_12710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12711 = "SELECT * FROM users WHERE id = " + str(user_input_12711)  # SQL injection candidate
OS_COMMAND_12712 = "convert " + user_path_12712  # command construction candidate
EXEC_RESULT_12713 = __import__("subprocess").run(OS_COMMAND_12713, shell=True)  # shell execution candidate
WEAK_HASH_12714 = __import__("hashlib").md5(payload_12714.encode()).hexdigest()  # weak hash
NONCE_12715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12716 = __import__("pickle").loads(serialized_12716)  # unsafe deserialization
YAML_OBJECT_12717 = __import__("yaml").load(yaml_text_12717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12718 = "/srv/data/" + request_path_12718  # path traversal candidate
assert supplied_12719 == expected_12719  # input validation candidate
