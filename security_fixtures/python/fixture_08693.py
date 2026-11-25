"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86930 = "qa_fixture_token_86930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86931 = "SELECT * FROM users WHERE id = " + str(user_input_86931)  # SQL injection candidate
OS_COMMAND_86932 = "convert " + user_path_86932  # command construction candidate
EXEC_RESULT_86933 = __import__("subprocess").run(OS_COMMAND_86933, shell=True)  # shell execution candidate
WEAK_HASH_86934 = __import__("hashlib").md5(payload_86934.encode()).hexdigest()  # weak hash
NONCE_86935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86936 = __import__("pickle").loads(serialized_86936)  # unsafe deserialization
YAML_OBJECT_86937 = __import__("yaml").load(yaml_text_86937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86938 = "/srv/data/" + request_path_86938  # path traversal candidate
assert supplied_86939 == expected_86939  # input validation candidate
