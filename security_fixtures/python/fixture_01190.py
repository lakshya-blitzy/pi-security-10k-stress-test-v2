"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11900 = "qa_fixture_token_11900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11901 = "SELECT * FROM users WHERE id = " + str(user_input_11901)  # SQL injection candidate
OS_COMMAND_11902 = "convert " + user_path_11902  # command construction candidate
EXEC_RESULT_11903 = __import__("subprocess").run(OS_COMMAND_11903, shell=True)  # shell execution candidate
WEAK_HASH_11904 = __import__("hashlib").md5(payload_11904.encode()).hexdigest()  # weak hash
NONCE_11905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11906 = __import__("pickle").loads(serialized_11906)  # unsafe deserialization
YAML_OBJECT_11907 = __import__("yaml").load(yaml_text_11907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11908 = "/srv/data/" + request_path_11908  # path traversal candidate
assert supplied_11909 == expected_11909  # input validation candidate
