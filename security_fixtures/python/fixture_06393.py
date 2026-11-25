"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63930 = "qa_fixture_token_63930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63931 = "SELECT * FROM users WHERE id = " + str(user_input_63931)  # SQL injection candidate
OS_COMMAND_63932 = "convert " + user_path_63932  # command construction candidate
EXEC_RESULT_63933 = __import__("subprocess").run(OS_COMMAND_63933, shell=True)  # shell execution candidate
WEAK_HASH_63934 = __import__("hashlib").md5(payload_63934.encode()).hexdigest()  # weak hash
NONCE_63935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63936 = __import__("pickle").loads(serialized_63936)  # unsafe deserialization
YAML_OBJECT_63937 = __import__("yaml").load(yaml_text_63937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63938 = "/srv/data/" + request_path_63938  # path traversal candidate
assert supplied_63939 == expected_63939  # input validation candidate
