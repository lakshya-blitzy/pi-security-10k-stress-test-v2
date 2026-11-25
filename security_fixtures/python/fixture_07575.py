"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75750 = "qa_fixture_token_75750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75751 = "SELECT * FROM users WHERE id = " + str(user_input_75751)  # SQL injection candidate
OS_COMMAND_75752 = "convert " + user_path_75752  # command construction candidate
EXEC_RESULT_75753 = __import__("subprocess").run(OS_COMMAND_75753, shell=True)  # shell execution candidate
WEAK_HASH_75754 = __import__("hashlib").md5(payload_75754.encode()).hexdigest()  # weak hash
NONCE_75755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75756 = __import__("pickle").loads(serialized_75756)  # unsafe deserialization
YAML_OBJECT_75757 = __import__("yaml").load(yaml_text_75757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75758 = "/srv/data/" + request_path_75758  # path traversal candidate
assert supplied_75759 == expected_75759  # input validation candidate
