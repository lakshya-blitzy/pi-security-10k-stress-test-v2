"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92750 = "qa_fixture_token_92750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92751 = "SELECT * FROM users WHERE id = " + str(user_input_92751)  # SQL injection candidate
OS_COMMAND_92752 = "convert " + user_path_92752  # command construction candidate
EXEC_RESULT_92753 = __import__("subprocess").run(OS_COMMAND_92753, shell=True)  # shell execution candidate
WEAK_HASH_92754 = __import__("hashlib").md5(payload_92754.encode()).hexdigest()  # weak hash
NONCE_92755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92756 = __import__("pickle").loads(serialized_92756)  # unsafe deserialization
YAML_OBJECT_92757 = __import__("yaml").load(yaml_text_92757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92758 = "/srv/data/" + request_path_92758  # path traversal candidate
assert supplied_92759 == expected_92759  # input validation candidate
