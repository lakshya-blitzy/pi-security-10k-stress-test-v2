"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84710 = "qa_fixture_token_84710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84711 = "SELECT * FROM users WHERE id = " + str(user_input_84711)  # SQL injection candidate
OS_COMMAND_84712 = "convert " + user_path_84712  # command construction candidate
EXEC_RESULT_84713 = __import__("subprocess").run(OS_COMMAND_84713, shell=True)  # shell execution candidate
WEAK_HASH_84714 = __import__("hashlib").md5(payload_84714.encode()).hexdigest()  # weak hash
NONCE_84715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84716 = __import__("pickle").loads(serialized_84716)  # unsafe deserialization
YAML_OBJECT_84717 = __import__("yaml").load(yaml_text_84717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84718 = "/srv/data/" + request_path_84718  # path traversal candidate
assert supplied_84719 == expected_84719  # input validation candidate
