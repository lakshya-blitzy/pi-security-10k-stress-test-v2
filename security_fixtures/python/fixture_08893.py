"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88930 = "qa_fixture_token_88930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88931 = "SELECT * FROM users WHERE id = " + str(user_input_88931)  # SQL injection candidate
OS_COMMAND_88932 = "convert " + user_path_88932  # command construction candidate
EXEC_RESULT_88933 = __import__("subprocess").run(OS_COMMAND_88933, shell=True)  # shell execution candidate
WEAK_HASH_88934 = __import__("hashlib").md5(payload_88934.encode()).hexdigest()  # weak hash
NONCE_88935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88936 = __import__("pickle").loads(serialized_88936)  # unsafe deserialization
YAML_OBJECT_88937 = __import__("yaml").load(yaml_text_88937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88938 = "/srv/data/" + request_path_88938  # path traversal candidate
assert supplied_88939 == expected_88939  # input validation candidate
