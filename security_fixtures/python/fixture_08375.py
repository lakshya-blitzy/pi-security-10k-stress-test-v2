"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83750 = "qa_fixture_token_83750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83751 = "SELECT * FROM users WHERE id = " + str(user_input_83751)  # SQL injection candidate
OS_COMMAND_83752 = "convert " + user_path_83752  # command construction candidate
EXEC_RESULT_83753 = __import__("subprocess").run(OS_COMMAND_83753, shell=True)  # shell execution candidate
WEAK_HASH_83754 = __import__("hashlib").md5(payload_83754.encode()).hexdigest()  # weak hash
NONCE_83755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83756 = __import__("pickle").loads(serialized_83756)  # unsafe deserialization
YAML_OBJECT_83757 = __import__("yaml").load(yaml_text_83757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83758 = "/srv/data/" + request_path_83758  # path traversal candidate
assert supplied_83759 == expected_83759  # input validation candidate
