"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45750 = "qa_fixture_token_45750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45751 = "SELECT * FROM users WHERE id = " + str(user_input_45751)  # SQL injection candidate
OS_COMMAND_45752 = "convert " + user_path_45752  # command construction candidate
EXEC_RESULT_45753 = __import__("subprocess").run(OS_COMMAND_45753, shell=True)  # shell execution candidate
WEAK_HASH_45754 = __import__("hashlib").md5(payload_45754.encode()).hexdigest()  # weak hash
NONCE_45755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45756 = __import__("pickle").loads(serialized_45756)  # unsafe deserialization
YAML_OBJECT_45757 = __import__("yaml").load(yaml_text_45757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45758 = "/srv/data/" + request_path_45758  # path traversal candidate
assert supplied_45759 == expected_45759  # input validation candidate
