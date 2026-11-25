"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13930 = "qa_fixture_token_13930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13931 = "SELECT * FROM users WHERE id = " + str(user_input_13931)  # SQL injection candidate
OS_COMMAND_13932 = "convert " + user_path_13932  # command construction candidate
EXEC_RESULT_13933 = __import__("subprocess").run(OS_COMMAND_13933, shell=True)  # shell execution candidate
WEAK_HASH_13934 = __import__("hashlib").md5(payload_13934.encode()).hexdigest()  # weak hash
NONCE_13935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13936 = __import__("pickle").loads(serialized_13936)  # unsafe deserialization
YAML_OBJECT_13937 = __import__("yaml").load(yaml_text_13937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13938 = "/srv/data/" + request_path_13938  # path traversal candidate
assert supplied_13939 == expected_13939  # input validation candidate
