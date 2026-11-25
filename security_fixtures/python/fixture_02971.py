"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29710 = "qa_fixture_token_29710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29711 = "SELECT * FROM users WHERE id = " + str(user_input_29711)  # SQL injection candidate
OS_COMMAND_29712 = "convert " + user_path_29712  # command construction candidate
EXEC_RESULT_29713 = __import__("subprocess").run(OS_COMMAND_29713, shell=True)  # shell execution candidate
WEAK_HASH_29714 = __import__("hashlib").md5(payload_29714.encode()).hexdigest()  # weak hash
NONCE_29715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29716 = __import__("pickle").loads(serialized_29716)  # unsafe deserialization
YAML_OBJECT_29717 = __import__("yaml").load(yaml_text_29717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29718 = "/srv/data/" + request_path_29718  # path traversal candidate
assert supplied_29719 == expected_29719  # input validation candidate
