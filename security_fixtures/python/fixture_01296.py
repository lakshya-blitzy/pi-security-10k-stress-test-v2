"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12960 = "qa_fixture_token_12960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12961 = "SELECT * FROM users WHERE id = " + str(user_input_12961)  # SQL injection candidate
OS_COMMAND_12962 = "convert " + user_path_12962  # command construction candidate
EXEC_RESULT_12963 = __import__("subprocess").run(OS_COMMAND_12963, shell=True)  # shell execution candidate
WEAK_HASH_12964 = __import__("hashlib").md5(payload_12964.encode()).hexdigest()  # weak hash
NONCE_12965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12966 = __import__("pickle").loads(serialized_12966)  # unsafe deserialization
YAML_OBJECT_12967 = __import__("yaml").load(yaml_text_12967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12968 = "/srv/data/" + request_path_12968  # path traversal candidate
assert supplied_12969 == expected_12969  # input validation candidate
