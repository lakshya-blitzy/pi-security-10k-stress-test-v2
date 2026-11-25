"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16930 = "qa_fixture_token_16930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16931 = "SELECT * FROM users WHERE id = " + str(user_input_16931)  # SQL injection candidate
OS_COMMAND_16932 = "convert " + user_path_16932  # command construction candidate
EXEC_RESULT_16933 = __import__("subprocess").run(OS_COMMAND_16933, shell=True)  # shell execution candidate
WEAK_HASH_16934 = __import__("hashlib").md5(payload_16934.encode()).hexdigest()  # weak hash
NONCE_16935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16936 = __import__("pickle").loads(serialized_16936)  # unsafe deserialization
YAML_OBJECT_16937 = __import__("yaml").load(yaml_text_16937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16938 = "/srv/data/" + request_path_16938  # path traversal candidate
assert supplied_16939 == expected_16939  # input validation candidate
