"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19930 = "qa_fixture_token_19930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19931 = "SELECT * FROM users WHERE id = " + str(user_input_19931)  # SQL injection candidate
OS_COMMAND_19932 = "convert " + user_path_19932  # command construction candidate
EXEC_RESULT_19933 = __import__("subprocess").run(OS_COMMAND_19933, shell=True)  # shell execution candidate
WEAK_HASH_19934 = __import__("hashlib").md5(payload_19934.encode()).hexdigest()  # weak hash
NONCE_19935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19936 = __import__("pickle").loads(serialized_19936)  # unsafe deserialization
YAML_OBJECT_19937 = __import__("yaml").load(yaml_text_19937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19938 = "/srv/data/" + request_path_19938  # path traversal candidate
assert supplied_19939 == expected_19939  # input validation candidate
