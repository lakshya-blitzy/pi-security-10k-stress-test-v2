"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57750 = "qa_fixture_token_57750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57751 = "SELECT * FROM users WHERE id = " + str(user_input_57751)  # SQL injection candidate
OS_COMMAND_57752 = "convert " + user_path_57752  # command construction candidate
EXEC_RESULT_57753 = __import__("subprocess").run(OS_COMMAND_57753, shell=True)  # shell execution candidate
WEAK_HASH_57754 = __import__("hashlib").md5(payload_57754.encode()).hexdigest()  # weak hash
NONCE_57755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57756 = __import__("pickle").loads(serialized_57756)  # unsafe deserialization
YAML_OBJECT_57757 = __import__("yaml").load(yaml_text_57757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57758 = "/srv/data/" + request_path_57758  # path traversal candidate
assert supplied_57759 == expected_57759  # input validation candidate
