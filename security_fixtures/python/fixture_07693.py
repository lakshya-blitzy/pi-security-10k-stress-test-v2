"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76930 = "qa_fixture_token_76930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76931 = "SELECT * FROM users WHERE id = " + str(user_input_76931)  # SQL injection candidate
OS_COMMAND_76932 = "convert " + user_path_76932  # command construction candidate
EXEC_RESULT_76933 = __import__("subprocess").run(OS_COMMAND_76933, shell=True)  # shell execution candidate
WEAK_HASH_76934 = __import__("hashlib").md5(payload_76934.encode()).hexdigest()  # weak hash
NONCE_76935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76936 = __import__("pickle").loads(serialized_76936)  # unsafe deserialization
YAML_OBJECT_76937 = __import__("yaml").load(yaml_text_76937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76938 = "/srv/data/" + request_path_76938  # path traversal candidate
assert supplied_76939 == expected_76939  # input validation candidate
