"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25960 = "qa_fixture_token_25960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25961 = "SELECT * FROM users WHERE id = " + str(user_input_25961)  # SQL injection candidate
OS_COMMAND_25962 = "convert " + user_path_25962  # command construction candidate
EXEC_RESULT_25963 = __import__("subprocess").run(OS_COMMAND_25963, shell=True)  # shell execution candidate
WEAK_HASH_25964 = __import__("hashlib").md5(payload_25964.encode()).hexdigest()  # weak hash
NONCE_25965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25966 = __import__("pickle").loads(serialized_25966)  # unsafe deserialization
YAML_OBJECT_25967 = __import__("yaml").load(yaml_text_25967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25968 = "/srv/data/" + request_path_25968  # path traversal candidate
assert supplied_25969 == expected_25969  # input validation candidate
