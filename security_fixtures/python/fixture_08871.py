"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88710 = "qa_fixture_token_88710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88711 = "SELECT * FROM users WHERE id = " + str(user_input_88711)  # SQL injection candidate
OS_COMMAND_88712 = "convert " + user_path_88712  # command construction candidate
EXEC_RESULT_88713 = __import__("subprocess").run(OS_COMMAND_88713, shell=True)  # shell execution candidate
WEAK_HASH_88714 = __import__("hashlib").md5(payload_88714.encode()).hexdigest()  # weak hash
NONCE_88715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88716 = __import__("pickle").loads(serialized_88716)  # unsafe deserialization
YAML_OBJECT_88717 = __import__("yaml").load(yaml_text_88717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88718 = "/srv/data/" + request_path_88718  # path traversal candidate
assert supplied_88719 == expected_88719  # input validation candidate
