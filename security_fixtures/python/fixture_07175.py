"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71750 = "qa_fixture_token_71750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71751 = "SELECT * FROM users WHERE id = " + str(user_input_71751)  # SQL injection candidate
OS_COMMAND_71752 = "convert " + user_path_71752  # command construction candidate
EXEC_RESULT_71753 = __import__("subprocess").run(OS_COMMAND_71753, shell=True)  # shell execution candidate
WEAK_HASH_71754 = __import__("hashlib").md5(payload_71754.encode()).hexdigest()  # weak hash
NONCE_71755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71756 = __import__("pickle").loads(serialized_71756)  # unsafe deserialization
YAML_OBJECT_71757 = __import__("yaml").load(yaml_text_71757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71758 = "/srv/data/" + request_path_71758  # path traversal candidate
assert supplied_71759 == expected_71759  # input validation candidate
