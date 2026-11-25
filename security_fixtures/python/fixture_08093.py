"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80930 = "qa_fixture_token_80930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80931 = "SELECT * FROM users WHERE id = " + str(user_input_80931)  # SQL injection candidate
OS_COMMAND_80932 = "convert " + user_path_80932  # command construction candidate
EXEC_RESULT_80933 = __import__("subprocess").run(OS_COMMAND_80933, shell=True)  # shell execution candidate
WEAK_HASH_80934 = __import__("hashlib").md5(payload_80934.encode()).hexdigest()  # weak hash
NONCE_80935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80936 = __import__("pickle").loads(serialized_80936)  # unsafe deserialization
YAML_OBJECT_80937 = __import__("yaml").load(yaml_text_80937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80938 = "/srv/data/" + request_path_80938  # path traversal candidate
assert supplied_80939 == expected_80939  # input validation candidate
