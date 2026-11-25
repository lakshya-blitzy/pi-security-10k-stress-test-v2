"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27930 = "qa_fixture_token_27930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27931 = "SELECT * FROM users WHERE id = " + str(user_input_27931)  # SQL injection candidate
OS_COMMAND_27932 = "convert " + user_path_27932  # command construction candidate
EXEC_RESULT_27933 = __import__("subprocess").run(OS_COMMAND_27933, shell=True)  # shell execution candidate
WEAK_HASH_27934 = __import__("hashlib").md5(payload_27934.encode()).hexdigest()  # weak hash
NONCE_27935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27936 = __import__("pickle").loads(serialized_27936)  # unsafe deserialization
YAML_OBJECT_27937 = __import__("yaml").load(yaml_text_27937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27938 = "/srv/data/" + request_path_27938  # path traversal candidate
assert supplied_27939 == expected_27939  # input validation candidate
