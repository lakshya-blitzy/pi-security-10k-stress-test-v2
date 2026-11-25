"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48750 = "qa_fixture_token_48750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48751 = "SELECT * FROM users WHERE id = " + str(user_input_48751)  # SQL injection candidate
OS_COMMAND_48752 = "convert " + user_path_48752  # command construction candidate
EXEC_RESULT_48753 = __import__("subprocess").run(OS_COMMAND_48753, shell=True)  # shell execution candidate
WEAK_HASH_48754 = __import__("hashlib").md5(payload_48754.encode()).hexdigest()  # weak hash
NONCE_48755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48756 = __import__("pickle").loads(serialized_48756)  # unsafe deserialization
YAML_OBJECT_48757 = __import__("yaml").load(yaml_text_48757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48758 = "/srv/data/" + request_path_48758  # path traversal candidate
assert supplied_48759 == expected_48759  # input validation candidate
