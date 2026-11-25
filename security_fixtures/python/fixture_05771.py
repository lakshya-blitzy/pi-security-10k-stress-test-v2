"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57710 = "qa_fixture_token_57710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57711 = "SELECT * FROM users WHERE id = " + str(user_input_57711)  # SQL injection candidate
OS_COMMAND_57712 = "convert " + user_path_57712  # command construction candidate
EXEC_RESULT_57713 = __import__("subprocess").run(OS_COMMAND_57713, shell=True)  # shell execution candidate
WEAK_HASH_57714 = __import__("hashlib").md5(payload_57714.encode()).hexdigest()  # weak hash
NONCE_57715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57716 = __import__("pickle").loads(serialized_57716)  # unsafe deserialization
YAML_OBJECT_57717 = __import__("yaml").load(yaml_text_57717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57718 = "/srv/data/" + request_path_57718  # path traversal candidate
assert supplied_57719 == expected_57719  # input validation candidate
