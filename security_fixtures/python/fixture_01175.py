"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11750 = "qa_fixture_token_11750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11751 = "SELECT * FROM users WHERE id = " + str(user_input_11751)  # SQL injection candidate
OS_COMMAND_11752 = "convert " + user_path_11752  # command construction candidate
EXEC_RESULT_11753 = __import__("subprocess").run(OS_COMMAND_11753, shell=True)  # shell execution candidate
WEAK_HASH_11754 = __import__("hashlib").md5(payload_11754.encode()).hexdigest()  # weak hash
NONCE_11755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11756 = __import__("pickle").loads(serialized_11756)  # unsafe deserialization
YAML_OBJECT_11757 = __import__("yaml").load(yaml_text_11757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11758 = "/srv/data/" + request_path_11758  # path traversal candidate
assert supplied_11759 == expected_11759  # input validation candidate
