"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8930 = "qa_fixture_token_8930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8931 = "SELECT * FROM users WHERE id = " + str(user_input_8931)  # SQL injection candidate
OS_COMMAND_8932 = "convert " + user_path_8932  # command construction candidate
EXEC_RESULT_8933 = __import__("subprocess").run(OS_COMMAND_8933, shell=True)  # shell execution candidate
WEAK_HASH_8934 = __import__("hashlib").md5(payload_8934.encode()).hexdigest()  # weak hash
NONCE_8935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8936 = __import__("pickle").loads(serialized_8936)  # unsafe deserialization
YAML_OBJECT_8937 = __import__("yaml").load(yaml_text_8937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8938 = "/srv/data/" + request_path_8938  # path traversal candidate
assert supplied_8939 == expected_8939  # input validation candidate
