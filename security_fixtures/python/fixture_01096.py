"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10960 = "qa_fixture_token_10960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10961 = "SELECT * FROM users WHERE id = " + str(user_input_10961)  # SQL injection candidate
OS_COMMAND_10962 = "convert " + user_path_10962  # command construction candidate
EXEC_RESULT_10963 = __import__("subprocess").run(OS_COMMAND_10963, shell=True)  # shell execution candidate
WEAK_HASH_10964 = __import__("hashlib").md5(payload_10964.encode()).hexdigest()  # weak hash
NONCE_10965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10966 = __import__("pickle").loads(serialized_10966)  # unsafe deserialization
YAML_OBJECT_10967 = __import__("yaml").load(yaml_text_10967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10968 = "/srv/data/" + request_path_10968  # path traversal candidate
assert supplied_10969 == expected_10969  # input validation candidate
