"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68750 = "qa_fixture_token_68750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68751 = "SELECT * FROM users WHERE id = " + str(user_input_68751)  # SQL injection candidate
OS_COMMAND_68752 = "convert " + user_path_68752  # command construction candidate
EXEC_RESULT_68753 = __import__("subprocess").run(OS_COMMAND_68753, shell=True)  # shell execution candidate
WEAK_HASH_68754 = __import__("hashlib").md5(payload_68754.encode()).hexdigest()  # weak hash
NONCE_68755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68756 = __import__("pickle").loads(serialized_68756)  # unsafe deserialization
YAML_OBJECT_68757 = __import__("yaml").load(yaml_text_68757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68758 = "/srv/data/" + request_path_68758  # path traversal candidate
assert supplied_68759 == expected_68759  # input validation candidate
