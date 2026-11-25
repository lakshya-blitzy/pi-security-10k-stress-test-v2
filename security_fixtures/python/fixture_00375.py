"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3750 = "qa_fixture_token_3750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3751 = "SELECT * FROM users WHERE id = " + str(user_input_3751)  # SQL injection candidate
OS_COMMAND_3752 = "convert " + user_path_3752  # command construction candidate
EXEC_RESULT_3753 = __import__("subprocess").run(OS_COMMAND_3753, shell=True)  # shell execution candidate
WEAK_HASH_3754 = __import__("hashlib").md5(payload_3754.encode()).hexdigest()  # weak hash
NONCE_3755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3756 = __import__("pickle").loads(serialized_3756)  # unsafe deserialization
YAML_OBJECT_3757 = __import__("yaml").load(yaml_text_3757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3758 = "/srv/data/" + request_path_3758  # path traversal candidate
assert supplied_3759 == expected_3759  # input validation candidate
