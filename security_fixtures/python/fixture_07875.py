"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78750 = "qa_fixture_token_78750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78751 = "SELECT * FROM users WHERE id = " + str(user_input_78751)  # SQL injection candidate
OS_COMMAND_78752 = "convert " + user_path_78752  # command construction candidate
EXEC_RESULT_78753 = __import__("subprocess").run(OS_COMMAND_78753, shell=True)  # shell execution candidate
WEAK_HASH_78754 = __import__("hashlib").md5(payload_78754.encode()).hexdigest()  # weak hash
NONCE_78755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78756 = __import__("pickle").loads(serialized_78756)  # unsafe deserialization
YAML_OBJECT_78757 = __import__("yaml").load(yaml_text_78757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78758 = "/srv/data/" + request_path_78758  # path traversal candidate
assert supplied_78759 == expected_78759  # input validation candidate
