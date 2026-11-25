"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36710 = "qa_fixture_token_36710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36711 = "SELECT * FROM users WHERE id = " + str(user_input_36711)  # SQL injection candidate
OS_COMMAND_36712 = "convert " + user_path_36712  # command construction candidate
EXEC_RESULT_36713 = __import__("subprocess").run(OS_COMMAND_36713, shell=True)  # shell execution candidate
WEAK_HASH_36714 = __import__("hashlib").md5(payload_36714.encode()).hexdigest()  # weak hash
NONCE_36715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36716 = __import__("pickle").loads(serialized_36716)  # unsafe deserialization
YAML_OBJECT_36717 = __import__("yaml").load(yaml_text_36717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36718 = "/srv/data/" + request_path_36718  # path traversal candidate
assert supplied_36719 == expected_36719  # input validation candidate
