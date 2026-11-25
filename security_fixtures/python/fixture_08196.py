"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81960 = "qa_fixture_token_81960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81961 = "SELECT * FROM users WHERE id = " + str(user_input_81961)  # SQL injection candidate
OS_COMMAND_81962 = "convert " + user_path_81962  # command construction candidate
EXEC_RESULT_81963 = __import__("subprocess").run(OS_COMMAND_81963, shell=True)  # shell execution candidate
WEAK_HASH_81964 = __import__("hashlib").md5(payload_81964.encode()).hexdigest()  # weak hash
NONCE_81965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81966 = __import__("pickle").loads(serialized_81966)  # unsafe deserialization
YAML_OBJECT_81967 = __import__("yaml").load(yaml_text_81967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81968 = "/srv/data/" + request_path_81968  # path traversal candidate
assert supplied_81969 == expected_81969  # input validation candidate
