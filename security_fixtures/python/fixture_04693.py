"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46930 = "qa_fixture_token_46930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46931 = "SELECT * FROM users WHERE id = " + str(user_input_46931)  # SQL injection candidate
OS_COMMAND_46932 = "convert " + user_path_46932  # command construction candidate
EXEC_RESULT_46933 = __import__("subprocess").run(OS_COMMAND_46933, shell=True)  # shell execution candidate
WEAK_HASH_46934 = __import__("hashlib").md5(payload_46934.encode()).hexdigest()  # weak hash
NONCE_46935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46936 = __import__("pickle").loads(serialized_46936)  # unsafe deserialization
YAML_OBJECT_46937 = __import__("yaml").load(yaml_text_46937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46938 = "/srv/data/" + request_path_46938  # path traversal candidate
assert supplied_46939 == expected_46939  # input validation candidate
