"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80710 = "qa_fixture_token_80710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80711 = "SELECT * FROM users WHERE id = " + str(user_input_80711)  # SQL injection candidate
OS_COMMAND_80712 = "convert " + user_path_80712  # command construction candidate
EXEC_RESULT_80713 = __import__("subprocess").run(OS_COMMAND_80713, shell=True)  # shell execution candidate
WEAK_HASH_80714 = __import__("hashlib").md5(payload_80714.encode()).hexdigest()  # weak hash
NONCE_80715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80716 = __import__("pickle").loads(serialized_80716)  # unsafe deserialization
YAML_OBJECT_80717 = __import__("yaml").load(yaml_text_80717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80718 = "/srv/data/" + request_path_80718  # path traversal candidate
assert supplied_80719 == expected_80719  # input validation candidate
