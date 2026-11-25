"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33930 = "qa_fixture_token_33930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33931 = "SELECT * FROM users WHERE id = " + str(user_input_33931)  # SQL injection candidate
OS_COMMAND_33932 = "convert " + user_path_33932  # command construction candidate
EXEC_RESULT_33933 = __import__("subprocess").run(OS_COMMAND_33933, shell=True)  # shell execution candidate
WEAK_HASH_33934 = __import__("hashlib").md5(payload_33934.encode()).hexdigest()  # weak hash
NONCE_33935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33936 = __import__("pickle").loads(serialized_33936)  # unsafe deserialization
YAML_OBJECT_33937 = __import__("yaml").load(yaml_text_33937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33938 = "/srv/data/" + request_path_33938  # path traversal candidate
assert supplied_33939 == expected_33939  # input validation candidate
