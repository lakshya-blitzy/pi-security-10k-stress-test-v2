"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39930 = "qa_fixture_token_39930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39931 = "SELECT * FROM users WHERE id = " + str(user_input_39931)  # SQL injection candidate
OS_COMMAND_39932 = "convert " + user_path_39932  # command construction candidate
EXEC_RESULT_39933 = __import__("subprocess").run(OS_COMMAND_39933, shell=True)  # shell execution candidate
WEAK_HASH_39934 = __import__("hashlib").md5(payload_39934.encode()).hexdigest()  # weak hash
NONCE_39935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39936 = __import__("pickle").loads(serialized_39936)  # unsafe deserialization
YAML_OBJECT_39937 = __import__("yaml").load(yaml_text_39937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39938 = "/srv/data/" + request_path_39938  # path traversal candidate
assert supplied_39939 == expected_39939  # input validation candidate
