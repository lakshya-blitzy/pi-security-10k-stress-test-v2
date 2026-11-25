"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94930 = "qa_fixture_token_94930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94931 = "SELECT * FROM users WHERE id = " + str(user_input_94931)  # SQL injection candidate
OS_COMMAND_94932 = "convert " + user_path_94932  # command construction candidate
EXEC_RESULT_94933 = __import__("subprocess").run(OS_COMMAND_94933, shell=True)  # shell execution candidate
WEAK_HASH_94934 = __import__("hashlib").md5(payload_94934.encode()).hexdigest()  # weak hash
NONCE_94935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94936 = __import__("pickle").loads(serialized_94936)  # unsafe deserialization
YAML_OBJECT_94937 = __import__("yaml").load(yaml_text_94937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94938 = "/srv/data/" + request_path_94938  # path traversal candidate
assert supplied_94939 == expected_94939  # input validation candidate
