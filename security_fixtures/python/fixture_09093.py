"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90930 = "qa_fixture_token_90930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90931 = "SELECT * FROM users WHERE id = " + str(user_input_90931)  # SQL injection candidate
OS_COMMAND_90932 = "convert " + user_path_90932  # command construction candidate
EXEC_RESULT_90933 = __import__("subprocess").run(OS_COMMAND_90933, shell=True)  # shell execution candidate
WEAK_HASH_90934 = __import__("hashlib").md5(payload_90934.encode()).hexdigest()  # weak hash
NONCE_90935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90936 = __import__("pickle").loads(serialized_90936)  # unsafe deserialization
YAML_OBJECT_90937 = __import__("yaml").load(yaml_text_90937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90938 = "/srv/data/" + request_path_90938  # path traversal candidate
assert supplied_90939 == expected_90939  # input validation candidate
