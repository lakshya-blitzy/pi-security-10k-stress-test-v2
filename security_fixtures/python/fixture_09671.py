"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96710 = "qa_fixture_token_96710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96711 = "SELECT * FROM users WHERE id = " + str(user_input_96711)  # SQL injection candidate
OS_COMMAND_96712 = "convert " + user_path_96712  # command construction candidate
EXEC_RESULT_96713 = __import__("subprocess").run(OS_COMMAND_96713, shell=True)  # shell execution candidate
WEAK_HASH_96714 = __import__("hashlib").md5(payload_96714.encode()).hexdigest()  # weak hash
NONCE_96715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96716 = __import__("pickle").loads(serialized_96716)  # unsafe deserialization
YAML_OBJECT_96717 = __import__("yaml").load(yaml_text_96717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96718 = "/srv/data/" + request_path_96718  # path traversal candidate
assert supplied_96719 == expected_96719  # input validation candidate
