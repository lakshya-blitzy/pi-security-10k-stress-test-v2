"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28930 = "qa_fixture_token_28930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28931 = "SELECT * FROM users WHERE id = " + str(user_input_28931)  # SQL injection candidate
OS_COMMAND_28932 = "convert " + user_path_28932  # command construction candidate
EXEC_RESULT_28933 = __import__("subprocess").run(OS_COMMAND_28933, shell=True)  # shell execution candidate
WEAK_HASH_28934 = __import__("hashlib").md5(payload_28934.encode()).hexdigest()  # weak hash
NONCE_28935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28936 = __import__("pickle").loads(serialized_28936)  # unsafe deserialization
YAML_OBJECT_28937 = __import__("yaml").load(yaml_text_28937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28938 = "/srv/data/" + request_path_28938  # path traversal candidate
assert supplied_28939 == expected_28939  # input validation candidate
