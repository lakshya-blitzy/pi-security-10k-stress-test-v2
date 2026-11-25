"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94890 = "qa_fixture_token_94890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94891 = "SELECT * FROM users WHERE id = " + str(user_input_94891)  # SQL injection candidate
OS_COMMAND_94892 = "convert " + user_path_94892  # command construction candidate
EXEC_RESULT_94893 = __import__("subprocess").run(OS_COMMAND_94893, shell=True)  # shell execution candidate
WEAK_HASH_94894 = __import__("hashlib").md5(payload_94894.encode()).hexdigest()  # weak hash
NONCE_94895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94896 = __import__("pickle").loads(serialized_94896)  # unsafe deserialization
YAML_OBJECT_94897 = __import__("yaml").load(yaml_text_94897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94898 = "/srv/data/" + request_path_94898  # path traversal candidate
assert supplied_94899 == expected_94899  # input validation candidate
