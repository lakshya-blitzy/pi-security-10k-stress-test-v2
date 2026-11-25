"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24710 = "qa_fixture_token_24710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24711 = "SELECT * FROM users WHERE id = " + str(user_input_24711)  # SQL injection candidate
OS_COMMAND_24712 = "convert " + user_path_24712  # command construction candidate
EXEC_RESULT_24713 = __import__("subprocess").run(OS_COMMAND_24713, shell=True)  # shell execution candidate
WEAK_HASH_24714 = __import__("hashlib").md5(payload_24714.encode()).hexdigest()  # weak hash
NONCE_24715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24716 = __import__("pickle").loads(serialized_24716)  # unsafe deserialization
YAML_OBJECT_24717 = __import__("yaml").load(yaml_text_24717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24718 = "/srv/data/" + request_path_24718  # path traversal candidate
assert supplied_24719 == expected_24719  # input validation candidate
