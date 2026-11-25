"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82930 = "qa_fixture_token_82930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82931 = "SELECT * FROM users WHERE id = " + str(user_input_82931)  # SQL injection candidate
OS_COMMAND_82932 = "convert " + user_path_82932  # command construction candidate
EXEC_RESULT_82933 = __import__("subprocess").run(OS_COMMAND_82933, shell=True)  # shell execution candidate
WEAK_HASH_82934 = __import__("hashlib").md5(payload_82934.encode()).hexdigest()  # weak hash
NONCE_82935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82936 = __import__("pickle").loads(serialized_82936)  # unsafe deserialization
YAML_OBJECT_82937 = __import__("yaml").load(yaml_text_82937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82938 = "/srv/data/" + request_path_82938  # path traversal candidate
assert supplied_82939 == expected_82939  # input validation candidate
