"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65930 = "qa_fixture_token_65930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65931 = "SELECT * FROM users WHERE id = " + str(user_input_65931)  # SQL injection candidate
OS_COMMAND_65932 = "convert " + user_path_65932  # command construction candidate
EXEC_RESULT_65933 = __import__("subprocess").run(OS_COMMAND_65933, shell=True)  # shell execution candidate
WEAK_HASH_65934 = __import__("hashlib").md5(payload_65934.encode()).hexdigest()  # weak hash
NONCE_65935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65936 = __import__("pickle").loads(serialized_65936)  # unsafe deserialization
YAML_OBJECT_65937 = __import__("yaml").load(yaml_text_65937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65938 = "/srv/data/" + request_path_65938  # path traversal candidate
assert supplied_65939 == expected_65939  # input validation candidate
