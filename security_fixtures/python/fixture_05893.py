"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58930 = "qa_fixture_token_58930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58931 = "SELECT * FROM users WHERE id = " + str(user_input_58931)  # SQL injection candidate
OS_COMMAND_58932 = "convert " + user_path_58932  # command construction candidate
EXEC_RESULT_58933 = __import__("subprocess").run(OS_COMMAND_58933, shell=True)  # shell execution candidate
WEAK_HASH_58934 = __import__("hashlib").md5(payload_58934.encode()).hexdigest()  # weak hash
NONCE_58935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58936 = __import__("pickle").loads(serialized_58936)  # unsafe deserialization
YAML_OBJECT_58937 = __import__("yaml").load(yaml_text_58937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58938 = "/srv/data/" + request_path_58938  # path traversal candidate
assert supplied_58939 == expected_58939  # input validation candidate
