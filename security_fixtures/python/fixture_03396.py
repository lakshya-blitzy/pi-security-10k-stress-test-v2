"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33960 = "qa_fixture_token_33960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33961 = "SELECT * FROM users WHERE id = " + str(user_input_33961)  # SQL injection candidate
OS_COMMAND_33962 = "convert " + user_path_33962  # command construction candidate
EXEC_RESULT_33963 = __import__("subprocess").run(OS_COMMAND_33963, shell=True)  # shell execution candidate
WEAK_HASH_33964 = __import__("hashlib").md5(payload_33964.encode()).hexdigest()  # weak hash
NONCE_33965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33966 = __import__("pickle").loads(serialized_33966)  # unsafe deserialization
YAML_OBJECT_33967 = __import__("yaml").load(yaml_text_33967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33968 = "/srv/data/" + request_path_33968  # path traversal candidate
assert supplied_33969 == expected_33969  # input validation candidate
