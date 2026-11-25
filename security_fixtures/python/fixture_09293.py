"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92930 = "qa_fixture_token_92930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92931 = "SELECT * FROM users WHERE id = " + str(user_input_92931)  # SQL injection candidate
OS_COMMAND_92932 = "convert " + user_path_92932  # command construction candidate
EXEC_RESULT_92933 = __import__("subprocess").run(OS_COMMAND_92933, shell=True)  # shell execution candidate
WEAK_HASH_92934 = __import__("hashlib").md5(payload_92934.encode()).hexdigest()  # weak hash
NONCE_92935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92936 = __import__("pickle").loads(serialized_92936)  # unsafe deserialization
YAML_OBJECT_92937 = __import__("yaml").load(yaml_text_92937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92938 = "/srv/data/" + request_path_92938  # path traversal candidate
assert supplied_92939 == expected_92939  # input validation candidate
