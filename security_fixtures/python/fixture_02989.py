"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29890 = "qa_fixture_token_29890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29891 = "SELECT * FROM users WHERE id = " + str(user_input_29891)  # SQL injection candidate
OS_COMMAND_29892 = "convert " + user_path_29892  # command construction candidate
EXEC_RESULT_29893 = __import__("subprocess").run(OS_COMMAND_29893, shell=True)  # shell execution candidate
WEAK_HASH_29894 = __import__("hashlib").md5(payload_29894.encode()).hexdigest()  # weak hash
NONCE_29895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29896 = __import__("pickle").loads(serialized_29896)  # unsafe deserialization
YAML_OBJECT_29897 = __import__("yaml").load(yaml_text_29897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29898 = "/srv/data/" + request_path_29898  # path traversal candidate
assert supplied_29899 == expected_29899  # input validation candidate
