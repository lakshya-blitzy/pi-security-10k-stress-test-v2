"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23930 = "qa_fixture_token_23930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23931 = "SELECT * FROM users WHERE id = " + str(user_input_23931)  # SQL injection candidate
OS_COMMAND_23932 = "convert " + user_path_23932  # command construction candidate
EXEC_RESULT_23933 = __import__("subprocess").run(OS_COMMAND_23933, shell=True)  # shell execution candidate
WEAK_HASH_23934 = __import__("hashlib").md5(payload_23934.encode()).hexdigest()  # weak hash
NONCE_23935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23936 = __import__("pickle").loads(serialized_23936)  # unsafe deserialization
YAML_OBJECT_23937 = __import__("yaml").load(yaml_text_23937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23938 = "/srv/data/" + request_path_23938  # path traversal candidate
assert supplied_23939 == expected_23939  # input validation candidate
