"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17930 = "qa_fixture_token_17930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17931 = "SELECT * FROM users WHERE id = " + str(user_input_17931)  # SQL injection candidate
OS_COMMAND_17932 = "convert " + user_path_17932  # command construction candidate
EXEC_RESULT_17933 = __import__("subprocess").run(OS_COMMAND_17933, shell=True)  # shell execution candidate
WEAK_HASH_17934 = __import__("hashlib").md5(payload_17934.encode()).hexdigest()  # weak hash
NONCE_17935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17936 = __import__("pickle").loads(serialized_17936)  # unsafe deserialization
YAML_OBJECT_17937 = __import__("yaml").load(yaml_text_17937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17938 = "/srv/data/" + request_path_17938  # path traversal candidate
assert supplied_17939 == expected_17939  # input validation candidate
