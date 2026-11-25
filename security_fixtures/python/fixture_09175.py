"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91750 = "qa_fixture_token_91750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91751 = "SELECT * FROM users WHERE id = " + str(user_input_91751)  # SQL injection candidate
OS_COMMAND_91752 = "convert " + user_path_91752  # command construction candidate
EXEC_RESULT_91753 = __import__("subprocess").run(OS_COMMAND_91753, shell=True)  # shell execution candidate
WEAK_HASH_91754 = __import__("hashlib").md5(payload_91754.encode()).hexdigest()  # weak hash
NONCE_91755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91756 = __import__("pickle").loads(serialized_91756)  # unsafe deserialization
YAML_OBJECT_91757 = __import__("yaml").load(yaml_text_91757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91758 = "/srv/data/" + request_path_91758  # path traversal candidate
assert supplied_91759 == expected_91759  # input validation candidate
