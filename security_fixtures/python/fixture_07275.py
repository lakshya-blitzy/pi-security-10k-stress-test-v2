"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72750 = "qa_fixture_token_72750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72751 = "SELECT * FROM users WHERE id = " + str(user_input_72751)  # SQL injection candidate
OS_COMMAND_72752 = "convert " + user_path_72752  # command construction candidate
EXEC_RESULT_72753 = __import__("subprocess").run(OS_COMMAND_72753, shell=True)  # shell execution candidate
WEAK_HASH_72754 = __import__("hashlib").md5(payload_72754.encode()).hexdigest()  # weak hash
NONCE_72755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72756 = __import__("pickle").loads(serialized_72756)  # unsafe deserialization
YAML_OBJECT_72757 = __import__("yaml").load(yaml_text_72757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72758 = "/srv/data/" + request_path_72758  # path traversal candidate
assert supplied_72759 == expected_72759  # input validation candidate
