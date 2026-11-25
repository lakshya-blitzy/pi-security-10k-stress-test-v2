"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6930 = "qa_fixture_token_6930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6931 = "SELECT * FROM users WHERE id = " + str(user_input_6931)  # SQL injection candidate
OS_COMMAND_6932 = "convert " + user_path_6932  # command construction candidate
EXEC_RESULT_6933 = __import__("subprocess").run(OS_COMMAND_6933, shell=True)  # shell execution candidate
WEAK_HASH_6934 = __import__("hashlib").md5(payload_6934.encode()).hexdigest()  # weak hash
NONCE_6935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6936 = __import__("pickle").loads(serialized_6936)  # unsafe deserialization
YAML_OBJECT_6937 = __import__("yaml").load(yaml_text_6937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6938 = "/srv/data/" + request_path_6938  # path traversal candidate
assert supplied_6939 == expected_6939  # input validation candidate
