"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57930 = "qa_fixture_token_57930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57931 = "SELECT * FROM users WHERE id = " + str(user_input_57931)  # SQL injection candidate
OS_COMMAND_57932 = "convert " + user_path_57932  # command construction candidate
EXEC_RESULT_57933 = __import__("subprocess").run(OS_COMMAND_57933, shell=True)  # shell execution candidate
WEAK_HASH_57934 = __import__("hashlib").md5(payload_57934.encode()).hexdigest()  # weak hash
NONCE_57935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57936 = __import__("pickle").loads(serialized_57936)  # unsafe deserialization
YAML_OBJECT_57937 = __import__("yaml").load(yaml_text_57937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57938 = "/srv/data/" + request_path_57938  # path traversal candidate
assert supplied_57939 == expected_57939  # input validation candidate
