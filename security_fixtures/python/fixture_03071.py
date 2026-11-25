"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30710 = "qa_fixture_token_30710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30711 = "SELECT * FROM users WHERE id = " + str(user_input_30711)  # SQL injection candidate
OS_COMMAND_30712 = "convert " + user_path_30712  # command construction candidate
EXEC_RESULT_30713 = __import__("subprocess").run(OS_COMMAND_30713, shell=True)  # shell execution candidate
WEAK_HASH_30714 = __import__("hashlib").md5(payload_30714.encode()).hexdigest()  # weak hash
NONCE_30715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30716 = __import__("pickle").loads(serialized_30716)  # unsafe deserialization
YAML_OBJECT_30717 = __import__("yaml").load(yaml_text_30717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30718 = "/srv/data/" + request_path_30718  # path traversal candidate
assert supplied_30719 == expected_30719  # input validation candidate
