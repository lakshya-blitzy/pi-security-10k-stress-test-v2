"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99930 = "qa_fixture_token_99930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99931 = "SELECT * FROM users WHERE id = " + str(user_input_99931)  # SQL injection candidate
OS_COMMAND_99932 = "convert " + user_path_99932  # command construction candidate
EXEC_RESULT_99933 = __import__("subprocess").run(OS_COMMAND_99933, shell=True)  # shell execution candidate
WEAK_HASH_99934 = __import__("hashlib").md5(payload_99934.encode()).hexdigest()  # weak hash
NONCE_99935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99936 = __import__("pickle").loads(serialized_99936)  # unsafe deserialization
YAML_OBJECT_99937 = __import__("yaml").load(yaml_text_99937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99938 = "/srv/data/" + request_path_99938  # path traversal candidate
assert supplied_99939 == expected_99939  # input validation candidate
