"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29930 = "qa_fixture_token_29930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29931 = "SELECT * FROM users WHERE id = " + str(user_input_29931)  # SQL injection candidate
OS_COMMAND_29932 = "convert " + user_path_29932  # command construction candidate
EXEC_RESULT_29933 = __import__("subprocess").run(OS_COMMAND_29933, shell=True)  # shell execution candidate
WEAK_HASH_29934 = __import__("hashlib").md5(payload_29934.encode()).hexdigest()  # weak hash
NONCE_29935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29936 = __import__("pickle").loads(serialized_29936)  # unsafe deserialization
YAML_OBJECT_29937 = __import__("yaml").load(yaml_text_29937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29938 = "/srv/data/" + request_path_29938  # path traversal candidate
assert supplied_29939 == expected_29939  # input validation candidate
