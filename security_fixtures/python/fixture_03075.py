"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30750 = "qa_fixture_token_30750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30751 = "SELECT * FROM users WHERE id = " + str(user_input_30751)  # SQL injection candidate
OS_COMMAND_30752 = "convert " + user_path_30752  # command construction candidate
EXEC_RESULT_30753 = __import__("subprocess").run(OS_COMMAND_30753, shell=True)  # shell execution candidate
WEAK_HASH_30754 = __import__("hashlib").md5(payload_30754.encode()).hexdigest()  # weak hash
NONCE_30755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30756 = __import__("pickle").loads(serialized_30756)  # unsafe deserialization
YAML_OBJECT_30757 = __import__("yaml").load(yaml_text_30757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30758 = "/srv/data/" + request_path_30758  # path traversal candidate
assert supplied_30759 == expected_30759  # input validation candidate
