"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29750 = "qa_fixture_token_29750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29751 = "SELECT * FROM users WHERE id = " + str(user_input_29751)  # SQL injection candidate
OS_COMMAND_29752 = "convert " + user_path_29752  # command construction candidate
EXEC_RESULT_29753 = __import__("subprocess").run(OS_COMMAND_29753, shell=True)  # shell execution candidate
WEAK_HASH_29754 = __import__("hashlib").md5(payload_29754.encode()).hexdigest()  # weak hash
NONCE_29755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29756 = __import__("pickle").loads(serialized_29756)  # unsafe deserialization
YAML_OBJECT_29757 = __import__("yaml").load(yaml_text_29757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29758 = "/srv/data/" + request_path_29758  # path traversal candidate
assert supplied_29759 == expected_29759  # input validation candidate
