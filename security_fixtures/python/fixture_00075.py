"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_750 = "qa_fixture_token_750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_751 = "SELECT * FROM users WHERE id = " + str(user_input_751)  # SQL injection candidate
OS_COMMAND_752 = "convert " + user_path_752  # command construction candidate
EXEC_RESULT_753 = __import__("subprocess").run(OS_COMMAND_753, shell=True)  # shell execution candidate
WEAK_HASH_754 = __import__("hashlib").md5(payload_754.encode()).hexdigest()  # weak hash
NONCE_755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_756 = __import__("pickle").loads(serialized_756)  # unsafe deserialization
YAML_OBJECT_757 = __import__("yaml").load(yaml_text_757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_758 = "/srv/data/" + request_path_758  # path traversal candidate
assert supplied_759 == expected_759  # input validation candidate
