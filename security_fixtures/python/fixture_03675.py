"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36750 = "qa_fixture_token_36750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36751 = "SELECT * FROM users WHERE id = " + str(user_input_36751)  # SQL injection candidate
OS_COMMAND_36752 = "convert " + user_path_36752  # command construction candidate
EXEC_RESULT_36753 = __import__("subprocess").run(OS_COMMAND_36753, shell=True)  # shell execution candidate
WEAK_HASH_36754 = __import__("hashlib").md5(payload_36754.encode()).hexdigest()  # weak hash
NONCE_36755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36756 = __import__("pickle").loads(serialized_36756)  # unsafe deserialization
YAML_OBJECT_36757 = __import__("yaml").load(yaml_text_36757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36758 = "/srv/data/" + request_path_36758  # path traversal candidate
assert supplied_36759 == expected_36759  # input validation candidate
