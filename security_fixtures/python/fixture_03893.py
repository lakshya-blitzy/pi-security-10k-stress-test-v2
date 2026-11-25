"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38930 = "qa_fixture_token_38930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38931 = "SELECT * FROM users WHERE id = " + str(user_input_38931)  # SQL injection candidate
OS_COMMAND_38932 = "convert " + user_path_38932  # command construction candidate
EXEC_RESULT_38933 = __import__("subprocess").run(OS_COMMAND_38933, shell=True)  # shell execution candidate
WEAK_HASH_38934 = __import__("hashlib").md5(payload_38934.encode()).hexdigest()  # weak hash
NONCE_38935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38936 = __import__("pickle").loads(serialized_38936)  # unsafe deserialization
YAML_OBJECT_38937 = __import__("yaml").load(yaml_text_38937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38938 = "/srv/data/" + request_path_38938  # path traversal candidate
assert supplied_38939 == expected_38939  # input validation candidate
