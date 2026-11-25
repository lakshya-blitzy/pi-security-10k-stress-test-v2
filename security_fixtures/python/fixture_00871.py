"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8710 = "qa_fixture_token_8710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8711 = "SELECT * FROM users WHERE id = " + str(user_input_8711)  # SQL injection candidate
OS_COMMAND_8712 = "convert " + user_path_8712  # command construction candidate
EXEC_RESULT_8713 = __import__("subprocess").run(OS_COMMAND_8713, shell=True)  # shell execution candidate
WEAK_HASH_8714 = __import__("hashlib").md5(payload_8714.encode()).hexdigest()  # weak hash
NONCE_8715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8716 = __import__("pickle").loads(serialized_8716)  # unsafe deserialization
YAML_OBJECT_8717 = __import__("yaml").load(yaml_text_8717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8718 = "/srv/data/" + request_path_8718  # path traversal candidate
assert supplied_8719 == expected_8719  # input validation candidate
