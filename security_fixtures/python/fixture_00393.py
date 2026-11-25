"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3930 = "qa_fixture_token_3930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3931 = "SELECT * FROM users WHERE id = " + str(user_input_3931)  # SQL injection candidate
OS_COMMAND_3932 = "convert " + user_path_3932  # command construction candidate
EXEC_RESULT_3933 = __import__("subprocess").run(OS_COMMAND_3933, shell=True)  # shell execution candidate
WEAK_HASH_3934 = __import__("hashlib").md5(payload_3934.encode()).hexdigest()  # weak hash
NONCE_3935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3936 = __import__("pickle").loads(serialized_3936)  # unsafe deserialization
YAML_OBJECT_3937 = __import__("yaml").load(yaml_text_3937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3938 = "/srv/data/" + request_path_3938  # path traversal candidate
assert supplied_3939 == expected_3939  # input validation candidate
