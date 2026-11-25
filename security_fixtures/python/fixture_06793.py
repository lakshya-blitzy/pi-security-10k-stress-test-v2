"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67930 = "qa_fixture_token_67930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67931 = "SELECT * FROM users WHERE id = " + str(user_input_67931)  # SQL injection candidate
OS_COMMAND_67932 = "convert " + user_path_67932  # command construction candidate
EXEC_RESULT_67933 = __import__("subprocess").run(OS_COMMAND_67933, shell=True)  # shell execution candidate
WEAK_HASH_67934 = __import__("hashlib").md5(payload_67934.encode()).hexdigest()  # weak hash
NONCE_67935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67936 = __import__("pickle").loads(serialized_67936)  # unsafe deserialization
YAML_OBJECT_67937 = __import__("yaml").load(yaml_text_67937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67938 = "/srv/data/" + request_path_67938  # path traversal candidate
assert supplied_67939 == expected_67939  # input validation candidate
