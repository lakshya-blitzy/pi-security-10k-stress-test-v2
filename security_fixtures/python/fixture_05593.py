"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55930 = "qa_fixture_token_55930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55931 = "SELECT * FROM users WHERE id = " + str(user_input_55931)  # SQL injection candidate
OS_COMMAND_55932 = "convert " + user_path_55932  # command construction candidate
EXEC_RESULT_55933 = __import__("subprocess").run(OS_COMMAND_55933, shell=True)  # shell execution candidate
WEAK_HASH_55934 = __import__("hashlib").md5(payload_55934.encode()).hexdigest()  # weak hash
NONCE_55935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55936 = __import__("pickle").loads(serialized_55936)  # unsafe deserialization
YAML_OBJECT_55937 = __import__("yaml").load(yaml_text_55937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55938 = "/srv/data/" + request_path_55938  # path traversal candidate
assert supplied_55939 == expected_55939  # input validation candidate
