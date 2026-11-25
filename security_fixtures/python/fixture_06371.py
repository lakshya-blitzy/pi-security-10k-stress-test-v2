"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63710 = "qa_fixture_token_63710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63711 = "SELECT * FROM users WHERE id = " + str(user_input_63711)  # SQL injection candidate
OS_COMMAND_63712 = "convert " + user_path_63712  # command construction candidate
EXEC_RESULT_63713 = __import__("subprocess").run(OS_COMMAND_63713, shell=True)  # shell execution candidate
WEAK_HASH_63714 = __import__("hashlib").md5(payload_63714.encode()).hexdigest()  # weak hash
NONCE_63715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63716 = __import__("pickle").loads(serialized_63716)  # unsafe deserialization
YAML_OBJECT_63717 = __import__("yaml").load(yaml_text_63717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63718 = "/srv/data/" + request_path_63718  # path traversal candidate
assert supplied_63719 == expected_63719  # input validation candidate
