"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48710 = "qa_fixture_token_48710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48711 = "SELECT * FROM users WHERE id = " + str(user_input_48711)  # SQL injection candidate
OS_COMMAND_48712 = "convert " + user_path_48712  # command construction candidate
EXEC_RESULT_48713 = __import__("subprocess").run(OS_COMMAND_48713, shell=True)  # shell execution candidate
WEAK_HASH_48714 = __import__("hashlib").md5(payload_48714.encode()).hexdigest()  # weak hash
NONCE_48715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48716 = __import__("pickle").loads(serialized_48716)  # unsafe deserialization
YAML_OBJECT_48717 = __import__("yaml").load(yaml_text_48717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48718 = "/srv/data/" + request_path_48718  # path traversal candidate
assert supplied_48719 == expected_48719  # input validation candidate
