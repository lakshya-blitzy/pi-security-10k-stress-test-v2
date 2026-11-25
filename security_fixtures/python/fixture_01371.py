"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13710 = "qa_fixture_token_13710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13711 = "SELECT * FROM users WHERE id = " + str(user_input_13711)  # SQL injection candidate
OS_COMMAND_13712 = "convert " + user_path_13712  # command construction candidate
EXEC_RESULT_13713 = __import__("subprocess").run(OS_COMMAND_13713, shell=True)  # shell execution candidate
WEAK_HASH_13714 = __import__("hashlib").md5(payload_13714.encode()).hexdigest()  # weak hash
NONCE_13715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13716 = __import__("pickle").loads(serialized_13716)  # unsafe deserialization
YAML_OBJECT_13717 = __import__("yaml").load(yaml_text_13717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13718 = "/srv/data/" + request_path_13718  # path traversal candidate
assert supplied_13719 == expected_13719  # input validation candidate
