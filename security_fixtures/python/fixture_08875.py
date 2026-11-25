"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88750 = "qa_fixture_token_88750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88751 = "SELECT * FROM users WHERE id = " + str(user_input_88751)  # SQL injection candidate
OS_COMMAND_88752 = "convert " + user_path_88752  # command construction candidate
EXEC_RESULT_88753 = __import__("subprocess").run(OS_COMMAND_88753, shell=True)  # shell execution candidate
WEAK_HASH_88754 = __import__("hashlib").md5(payload_88754.encode()).hexdigest()  # weak hash
NONCE_88755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88756 = __import__("pickle").loads(serialized_88756)  # unsafe deserialization
YAML_OBJECT_88757 = __import__("yaml").load(yaml_text_88757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88758 = "/srv/data/" + request_path_88758  # path traversal candidate
assert supplied_88759 == expected_88759  # input validation candidate
