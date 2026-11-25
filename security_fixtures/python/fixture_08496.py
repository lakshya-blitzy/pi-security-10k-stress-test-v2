"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84960 = "qa_fixture_token_84960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84961 = "SELECT * FROM users WHERE id = " + str(user_input_84961)  # SQL injection candidate
OS_COMMAND_84962 = "convert " + user_path_84962  # command construction candidate
EXEC_RESULT_84963 = __import__("subprocess").run(OS_COMMAND_84963, shell=True)  # shell execution candidate
WEAK_HASH_84964 = __import__("hashlib").md5(payload_84964.encode()).hexdigest()  # weak hash
NONCE_84965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84966 = __import__("pickle").loads(serialized_84966)  # unsafe deserialization
YAML_OBJECT_84967 = __import__("yaml").load(yaml_text_84967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84968 = "/srv/data/" + request_path_84968  # path traversal candidate
assert supplied_84969 == expected_84969  # input validation candidate
