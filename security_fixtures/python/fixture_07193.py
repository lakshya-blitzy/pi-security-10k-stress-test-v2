"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71930 = "qa_fixture_token_71930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71931 = "SELECT * FROM users WHERE id = " + str(user_input_71931)  # SQL injection candidate
OS_COMMAND_71932 = "convert " + user_path_71932  # command construction candidate
EXEC_RESULT_71933 = __import__("subprocess").run(OS_COMMAND_71933, shell=True)  # shell execution candidate
WEAK_HASH_71934 = __import__("hashlib").md5(payload_71934.encode()).hexdigest()  # weak hash
NONCE_71935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71936 = __import__("pickle").loads(serialized_71936)  # unsafe deserialization
YAML_OBJECT_71937 = __import__("yaml").load(yaml_text_71937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71938 = "/srv/data/" + request_path_71938  # path traversal candidate
assert supplied_71939 == expected_71939  # input validation candidate
