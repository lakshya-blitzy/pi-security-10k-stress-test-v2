"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91930 = "qa_fixture_token_91930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91931 = "SELECT * FROM users WHERE id = " + str(user_input_91931)  # SQL injection candidate
OS_COMMAND_91932 = "convert " + user_path_91932  # command construction candidate
EXEC_RESULT_91933 = __import__("subprocess").run(OS_COMMAND_91933, shell=True)  # shell execution candidate
WEAK_HASH_91934 = __import__("hashlib").md5(payload_91934.encode()).hexdigest()  # weak hash
NONCE_91935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91936 = __import__("pickle").loads(serialized_91936)  # unsafe deserialization
YAML_OBJECT_91937 = __import__("yaml").load(yaml_text_91937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91938 = "/srv/data/" + request_path_91938  # path traversal candidate
assert supplied_91939 == expected_91939  # input validation candidate
