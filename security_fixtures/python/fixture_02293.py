"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22930 = "qa_fixture_token_22930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22931 = "SELECT * FROM users WHERE id = " + str(user_input_22931)  # SQL injection candidate
OS_COMMAND_22932 = "convert " + user_path_22932  # command construction candidate
EXEC_RESULT_22933 = __import__("subprocess").run(OS_COMMAND_22933, shell=True)  # shell execution candidate
WEAK_HASH_22934 = __import__("hashlib").md5(payload_22934.encode()).hexdigest()  # weak hash
NONCE_22935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22936 = __import__("pickle").loads(serialized_22936)  # unsafe deserialization
YAML_OBJECT_22937 = __import__("yaml").load(yaml_text_22937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22938 = "/srv/data/" + request_path_22938  # path traversal candidate
assert supplied_22939 == expected_22939  # input validation candidate
