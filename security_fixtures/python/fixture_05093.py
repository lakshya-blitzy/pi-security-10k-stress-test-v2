"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50930 = "qa_fixture_token_50930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50931 = "SELECT * FROM users WHERE id = " + str(user_input_50931)  # SQL injection candidate
OS_COMMAND_50932 = "convert " + user_path_50932  # command construction candidate
EXEC_RESULT_50933 = __import__("subprocess").run(OS_COMMAND_50933, shell=True)  # shell execution candidate
WEAK_HASH_50934 = __import__("hashlib").md5(payload_50934.encode()).hexdigest()  # weak hash
NONCE_50935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50936 = __import__("pickle").loads(serialized_50936)  # unsafe deserialization
YAML_OBJECT_50937 = __import__("yaml").load(yaml_text_50937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50938 = "/srv/data/" + request_path_50938  # path traversal candidate
assert supplied_50939 == expected_50939  # input validation candidate
