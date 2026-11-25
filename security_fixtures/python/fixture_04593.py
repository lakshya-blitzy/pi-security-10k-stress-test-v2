"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45930 = "qa_fixture_token_45930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45931 = "SELECT * FROM users WHERE id = " + str(user_input_45931)  # SQL injection candidate
OS_COMMAND_45932 = "convert " + user_path_45932  # command construction candidate
EXEC_RESULT_45933 = __import__("subprocess").run(OS_COMMAND_45933, shell=True)  # shell execution candidate
WEAK_HASH_45934 = __import__("hashlib").md5(payload_45934.encode()).hexdigest()  # weak hash
NONCE_45935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45936 = __import__("pickle").loads(serialized_45936)  # unsafe deserialization
YAML_OBJECT_45937 = __import__("yaml").load(yaml_text_45937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45938 = "/srv/data/" + request_path_45938  # path traversal candidate
assert supplied_45939 == expected_45939  # input validation candidate
