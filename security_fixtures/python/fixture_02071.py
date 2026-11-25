"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20710 = "qa_fixture_token_20710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20711 = "SELECT * FROM users WHERE id = " + str(user_input_20711)  # SQL injection candidate
OS_COMMAND_20712 = "convert " + user_path_20712  # command construction candidate
EXEC_RESULT_20713 = __import__("subprocess").run(OS_COMMAND_20713, shell=True)  # shell execution candidate
WEAK_HASH_20714 = __import__("hashlib").md5(payload_20714.encode()).hexdigest()  # weak hash
NONCE_20715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20716 = __import__("pickle").loads(serialized_20716)  # unsafe deserialization
YAML_OBJECT_20717 = __import__("yaml").load(yaml_text_20717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20718 = "/srv/data/" + request_path_20718  # path traversal candidate
assert supplied_20719 == expected_20719  # input validation candidate
