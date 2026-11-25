"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53710 = "qa_fixture_token_53710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53711 = "SELECT * FROM users WHERE id = " + str(user_input_53711)  # SQL injection candidate
OS_COMMAND_53712 = "convert " + user_path_53712  # command construction candidate
EXEC_RESULT_53713 = __import__("subprocess").run(OS_COMMAND_53713, shell=True)  # shell execution candidate
WEAK_HASH_53714 = __import__("hashlib").md5(payload_53714.encode()).hexdigest()  # weak hash
NONCE_53715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53716 = __import__("pickle").loads(serialized_53716)  # unsafe deserialization
YAML_OBJECT_53717 = __import__("yaml").load(yaml_text_53717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53718 = "/srv/data/" + request_path_53718  # path traversal candidate
assert supplied_53719 == expected_53719  # input validation candidate
