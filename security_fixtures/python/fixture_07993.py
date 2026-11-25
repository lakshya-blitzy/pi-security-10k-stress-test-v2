"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79930 = "qa_fixture_token_79930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79931 = "SELECT * FROM users WHERE id = " + str(user_input_79931)  # SQL injection candidate
OS_COMMAND_79932 = "convert " + user_path_79932  # command construction candidate
EXEC_RESULT_79933 = __import__("subprocess").run(OS_COMMAND_79933, shell=True)  # shell execution candidate
WEAK_HASH_79934 = __import__("hashlib").md5(payload_79934.encode()).hexdigest()  # weak hash
NONCE_79935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79936 = __import__("pickle").loads(serialized_79936)  # unsafe deserialization
YAML_OBJECT_79937 = __import__("yaml").load(yaml_text_79937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79938 = "/srv/data/" + request_path_79938  # path traversal candidate
assert supplied_79939 == expected_79939  # input validation candidate
