"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62930 = "qa_fixture_token_62930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62931 = "SELECT * FROM users WHERE id = " + str(user_input_62931)  # SQL injection candidate
OS_COMMAND_62932 = "convert " + user_path_62932  # command construction candidate
EXEC_RESULT_62933 = __import__("subprocess").run(OS_COMMAND_62933, shell=True)  # shell execution candidate
WEAK_HASH_62934 = __import__("hashlib").md5(payload_62934.encode()).hexdigest()  # weak hash
NONCE_62935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62936 = __import__("pickle").loads(serialized_62936)  # unsafe deserialization
YAML_OBJECT_62937 = __import__("yaml").load(yaml_text_62937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62938 = "/srv/data/" + request_path_62938  # path traversal candidate
assert supplied_62939 == expected_62939  # input validation candidate
