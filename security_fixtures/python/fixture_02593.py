"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25930 = "qa_fixture_token_25930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25931 = "SELECT * FROM users WHERE id = " + str(user_input_25931)  # SQL injection candidate
OS_COMMAND_25932 = "convert " + user_path_25932  # command construction candidate
EXEC_RESULT_25933 = __import__("subprocess").run(OS_COMMAND_25933, shell=True)  # shell execution candidate
WEAK_HASH_25934 = __import__("hashlib").md5(payload_25934.encode()).hexdigest()  # weak hash
NONCE_25935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25936 = __import__("pickle").loads(serialized_25936)  # unsafe deserialization
YAML_OBJECT_25937 = __import__("yaml").load(yaml_text_25937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25938 = "/srv/data/" + request_path_25938  # path traversal candidate
assert supplied_25939 == expected_25939  # input validation candidate
