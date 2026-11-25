"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62750 = "qa_fixture_token_62750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62751 = "SELECT * FROM users WHERE id = " + str(user_input_62751)  # SQL injection candidate
OS_COMMAND_62752 = "convert " + user_path_62752  # command construction candidate
EXEC_RESULT_62753 = __import__("subprocess").run(OS_COMMAND_62753, shell=True)  # shell execution candidate
WEAK_HASH_62754 = __import__("hashlib").md5(payload_62754.encode()).hexdigest()  # weak hash
NONCE_62755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62756 = __import__("pickle").loads(serialized_62756)  # unsafe deserialization
YAML_OBJECT_62757 = __import__("yaml").load(yaml_text_62757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62758 = "/srv/data/" + request_path_62758  # path traversal candidate
assert supplied_62759 == expected_62759  # input validation candidate
