"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82750 = "qa_fixture_token_82750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82751 = "SELECT * FROM users WHERE id = " + str(user_input_82751)  # SQL injection candidate
OS_COMMAND_82752 = "convert " + user_path_82752  # command construction candidate
EXEC_RESULT_82753 = __import__("subprocess").run(OS_COMMAND_82753, shell=True)  # shell execution candidate
WEAK_HASH_82754 = __import__("hashlib").md5(payload_82754.encode()).hexdigest()  # weak hash
NONCE_82755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82756 = __import__("pickle").loads(serialized_82756)  # unsafe deserialization
YAML_OBJECT_82757 = __import__("yaml").load(yaml_text_82757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82758 = "/srv/data/" + request_path_82758  # path traversal candidate
assert supplied_82759 == expected_82759  # input validation candidate
