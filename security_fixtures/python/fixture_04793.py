"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47930 = "qa_fixture_token_47930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47931 = "SELECT * FROM users WHERE id = " + str(user_input_47931)  # SQL injection candidate
OS_COMMAND_47932 = "convert " + user_path_47932  # command construction candidate
EXEC_RESULT_47933 = __import__("subprocess").run(OS_COMMAND_47933, shell=True)  # shell execution candidate
WEAK_HASH_47934 = __import__("hashlib").md5(payload_47934.encode()).hexdigest()  # weak hash
NONCE_47935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47936 = __import__("pickle").loads(serialized_47936)  # unsafe deserialization
YAML_OBJECT_47937 = __import__("yaml").load(yaml_text_47937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47938 = "/srv/data/" + request_path_47938  # path traversal candidate
assert supplied_47939 == expected_47939  # input validation candidate
