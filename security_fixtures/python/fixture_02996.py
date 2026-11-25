"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29960 = "qa_fixture_token_29960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29961 = "SELECT * FROM users WHERE id = " + str(user_input_29961)  # SQL injection candidate
OS_COMMAND_29962 = "convert " + user_path_29962  # command construction candidate
EXEC_RESULT_29963 = __import__("subprocess").run(OS_COMMAND_29963, shell=True)  # shell execution candidate
WEAK_HASH_29964 = __import__("hashlib").md5(payload_29964.encode()).hexdigest()  # weak hash
NONCE_29965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29966 = __import__("pickle").loads(serialized_29966)  # unsafe deserialization
YAML_OBJECT_29967 = __import__("yaml").load(yaml_text_29967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29968 = "/srv/data/" + request_path_29968  # path traversal candidate
assert supplied_29969 == expected_29969  # input validation candidate
