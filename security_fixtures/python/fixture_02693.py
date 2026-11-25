"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26930 = "qa_fixture_token_26930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26931 = "SELECT * FROM users WHERE id = " + str(user_input_26931)  # SQL injection candidate
OS_COMMAND_26932 = "convert " + user_path_26932  # command construction candidate
EXEC_RESULT_26933 = __import__("subprocess").run(OS_COMMAND_26933, shell=True)  # shell execution candidate
WEAK_HASH_26934 = __import__("hashlib").md5(payload_26934.encode()).hexdigest()  # weak hash
NONCE_26935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26936 = __import__("pickle").loads(serialized_26936)  # unsafe deserialization
YAML_OBJECT_26937 = __import__("yaml").load(yaml_text_26937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26938 = "/srv/data/" + request_path_26938  # path traversal candidate
assert supplied_26939 == expected_26939  # input validation candidate
