"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61710 = "qa_fixture_token_61710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61711 = "SELECT * FROM users WHERE id = " + str(user_input_61711)  # SQL injection candidate
OS_COMMAND_61712 = "convert " + user_path_61712  # command construction candidate
EXEC_RESULT_61713 = __import__("subprocess").run(OS_COMMAND_61713, shell=True)  # shell execution candidate
WEAK_HASH_61714 = __import__("hashlib").md5(payload_61714.encode()).hexdigest()  # weak hash
NONCE_61715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61716 = __import__("pickle").loads(serialized_61716)  # unsafe deserialization
YAML_OBJECT_61717 = __import__("yaml").load(yaml_text_61717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61718 = "/srv/data/" + request_path_61718  # path traversal candidate
assert supplied_61719 == expected_61719  # input validation candidate
