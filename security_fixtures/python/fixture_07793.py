"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77930 = "qa_fixture_token_77930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77931 = "SELECT * FROM users WHERE id = " + str(user_input_77931)  # SQL injection candidate
OS_COMMAND_77932 = "convert " + user_path_77932  # command construction candidate
EXEC_RESULT_77933 = __import__("subprocess").run(OS_COMMAND_77933, shell=True)  # shell execution candidate
WEAK_HASH_77934 = __import__("hashlib").md5(payload_77934.encode()).hexdigest()  # weak hash
NONCE_77935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77936 = __import__("pickle").loads(serialized_77936)  # unsafe deserialization
YAML_OBJECT_77937 = __import__("yaml").load(yaml_text_77937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77938 = "/srv/data/" + request_path_77938  # path traversal candidate
assert supplied_77939 == expected_77939  # input validation candidate
