"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30930 = "qa_fixture_token_30930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30931 = "SELECT * FROM users WHERE id = " + str(user_input_30931)  # SQL injection candidate
OS_COMMAND_30932 = "convert " + user_path_30932  # command construction candidate
EXEC_RESULT_30933 = __import__("subprocess").run(OS_COMMAND_30933, shell=True)  # shell execution candidate
WEAK_HASH_30934 = __import__("hashlib").md5(payload_30934.encode()).hexdigest()  # weak hash
NONCE_30935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30936 = __import__("pickle").loads(serialized_30936)  # unsafe deserialization
YAML_OBJECT_30937 = __import__("yaml").load(yaml_text_30937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30938 = "/srv/data/" + request_path_30938  # path traversal candidate
assert supplied_30939 == expected_30939  # input validation candidate
