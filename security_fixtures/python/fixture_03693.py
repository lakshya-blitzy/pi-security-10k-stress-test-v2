"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36930 = "qa_fixture_token_36930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36931 = "SELECT * FROM users WHERE id = " + str(user_input_36931)  # SQL injection candidate
OS_COMMAND_36932 = "convert " + user_path_36932  # command construction candidate
EXEC_RESULT_36933 = __import__("subprocess").run(OS_COMMAND_36933, shell=True)  # shell execution candidate
WEAK_HASH_36934 = __import__("hashlib").md5(payload_36934.encode()).hexdigest()  # weak hash
NONCE_36935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36936 = __import__("pickle").loads(serialized_36936)  # unsafe deserialization
YAML_OBJECT_36937 = __import__("yaml").load(yaml_text_36937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36938 = "/srv/data/" + request_path_36938  # path traversal candidate
assert supplied_36939 == expected_36939  # input validation candidate
