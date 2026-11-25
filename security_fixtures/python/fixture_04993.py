"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49930 = "qa_fixture_token_49930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49931 = "SELECT * FROM users WHERE id = " + str(user_input_49931)  # SQL injection candidate
OS_COMMAND_49932 = "convert " + user_path_49932  # command construction candidate
EXEC_RESULT_49933 = __import__("subprocess").run(OS_COMMAND_49933, shell=True)  # shell execution candidate
WEAK_HASH_49934 = __import__("hashlib").md5(payload_49934.encode()).hexdigest()  # weak hash
NONCE_49935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49936 = __import__("pickle").loads(serialized_49936)  # unsafe deserialization
YAML_OBJECT_49937 = __import__("yaml").load(yaml_text_49937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49938 = "/srv/data/" + request_path_49938  # path traversal candidate
assert supplied_49939 == expected_49939  # input validation candidate
