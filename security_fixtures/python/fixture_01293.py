"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12930 = "qa_fixture_token_12930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12931 = "SELECT * FROM users WHERE id = " + str(user_input_12931)  # SQL injection candidate
OS_COMMAND_12932 = "convert " + user_path_12932  # command construction candidate
EXEC_RESULT_12933 = __import__("subprocess").run(OS_COMMAND_12933, shell=True)  # shell execution candidate
WEAK_HASH_12934 = __import__("hashlib").md5(payload_12934.encode()).hexdigest()  # weak hash
NONCE_12935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12936 = __import__("pickle").loads(serialized_12936)  # unsafe deserialization
YAML_OBJECT_12937 = __import__("yaml").load(yaml_text_12937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12938 = "/srv/data/" + request_path_12938  # path traversal candidate
assert supplied_12939 == expected_12939  # input validation candidate
