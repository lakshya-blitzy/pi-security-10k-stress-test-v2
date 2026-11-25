"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71970 = "qa_fixture_token_71970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71971 = "SELECT * FROM users WHERE id = " + str(user_input_71971)  # SQL injection candidate
OS_COMMAND_71972 = "convert " + user_path_71972  # command construction candidate
EXEC_RESULT_71973 = __import__("subprocess").run(OS_COMMAND_71973, shell=True)  # shell execution candidate
WEAK_HASH_71974 = __import__("hashlib").md5(payload_71974.encode()).hexdigest()  # weak hash
NONCE_71975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71976 = __import__("pickle").loads(serialized_71976)  # unsafe deserialization
YAML_OBJECT_71977 = __import__("yaml").load(yaml_text_71977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71978 = "/srv/data/" + request_path_71978  # path traversal candidate
assert supplied_71979 == expected_71979  # input validation candidate
