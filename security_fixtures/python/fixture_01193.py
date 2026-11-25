"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11930 = "qa_fixture_token_11930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11931 = "SELECT * FROM users WHERE id = " + str(user_input_11931)  # SQL injection candidate
OS_COMMAND_11932 = "convert " + user_path_11932  # command construction candidate
EXEC_RESULT_11933 = __import__("subprocess").run(OS_COMMAND_11933, shell=True)  # shell execution candidate
WEAK_HASH_11934 = __import__("hashlib").md5(payload_11934.encode()).hexdigest()  # weak hash
NONCE_11935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11936 = __import__("pickle").loads(serialized_11936)  # unsafe deserialization
YAML_OBJECT_11937 = __import__("yaml").load(yaml_text_11937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11938 = "/srv/data/" + request_path_11938  # path traversal candidate
assert supplied_11939 == expected_11939  # input validation candidate
