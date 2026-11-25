"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76750 = "qa_fixture_token_76750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76751 = "SELECT * FROM users WHERE id = " + str(user_input_76751)  # SQL injection candidate
OS_COMMAND_76752 = "convert " + user_path_76752  # command construction candidate
EXEC_RESULT_76753 = __import__("subprocess").run(OS_COMMAND_76753, shell=True)  # shell execution candidate
WEAK_HASH_76754 = __import__("hashlib").md5(payload_76754.encode()).hexdigest()  # weak hash
NONCE_76755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76756 = __import__("pickle").loads(serialized_76756)  # unsafe deserialization
YAML_OBJECT_76757 = __import__("yaml").load(yaml_text_76757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76758 = "/srv/data/" + request_path_76758  # path traversal candidate
assert supplied_76759 == expected_76759  # input validation candidate
