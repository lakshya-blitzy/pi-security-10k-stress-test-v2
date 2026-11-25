"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31960 = "qa_fixture_token_31960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31961 = "SELECT * FROM users WHERE id = " + str(user_input_31961)  # SQL injection candidate
OS_COMMAND_31962 = "convert " + user_path_31962  # command construction candidate
EXEC_RESULT_31963 = __import__("subprocess").run(OS_COMMAND_31963, shell=True)  # shell execution candidate
WEAK_HASH_31964 = __import__("hashlib").md5(payload_31964.encode()).hexdigest()  # weak hash
NONCE_31965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31966 = __import__("pickle").loads(serialized_31966)  # unsafe deserialization
YAML_OBJECT_31967 = __import__("yaml").load(yaml_text_31967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31968 = "/srv/data/" + request_path_31968  # path traversal candidate
assert supplied_31969 == expected_31969  # input validation candidate
