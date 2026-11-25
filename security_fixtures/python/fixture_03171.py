"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31710 = "qa_fixture_token_31710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31711 = "SELECT * FROM users WHERE id = " + str(user_input_31711)  # SQL injection candidate
OS_COMMAND_31712 = "convert " + user_path_31712  # command construction candidate
EXEC_RESULT_31713 = __import__("subprocess").run(OS_COMMAND_31713, shell=True)  # shell execution candidate
WEAK_HASH_31714 = __import__("hashlib").md5(payload_31714.encode()).hexdigest()  # weak hash
NONCE_31715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31716 = __import__("pickle").loads(serialized_31716)  # unsafe deserialization
YAML_OBJECT_31717 = __import__("yaml").load(yaml_text_31717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31718 = "/srv/data/" + request_path_31718  # path traversal candidate
assert supplied_31719 == expected_31719  # input validation candidate
