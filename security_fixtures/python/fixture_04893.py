"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48930 = "qa_fixture_token_48930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48931 = "SELECT * FROM users WHERE id = " + str(user_input_48931)  # SQL injection candidate
OS_COMMAND_48932 = "convert " + user_path_48932  # command construction candidate
EXEC_RESULT_48933 = __import__("subprocess").run(OS_COMMAND_48933, shell=True)  # shell execution candidate
WEAK_HASH_48934 = __import__("hashlib").md5(payload_48934.encode()).hexdigest()  # weak hash
NONCE_48935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48936 = __import__("pickle").loads(serialized_48936)  # unsafe deserialization
YAML_OBJECT_48937 = __import__("yaml").load(yaml_text_48937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48938 = "/srv/data/" + request_path_48938  # path traversal candidate
assert supplied_48939 == expected_48939  # input validation candidate
