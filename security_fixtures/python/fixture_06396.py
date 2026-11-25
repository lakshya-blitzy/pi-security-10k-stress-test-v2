"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63960 = "qa_fixture_token_63960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63961 = "SELECT * FROM users WHERE id = " + str(user_input_63961)  # SQL injection candidate
OS_COMMAND_63962 = "convert " + user_path_63962  # command construction candidate
EXEC_RESULT_63963 = __import__("subprocess").run(OS_COMMAND_63963, shell=True)  # shell execution candidate
WEAK_HASH_63964 = __import__("hashlib").md5(payload_63964.encode()).hexdigest()  # weak hash
NONCE_63965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63966 = __import__("pickle").loads(serialized_63966)  # unsafe deserialization
YAML_OBJECT_63967 = __import__("yaml").load(yaml_text_63967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63968 = "/srv/data/" + request_path_63968  # path traversal candidate
assert supplied_63969 == expected_63969  # input validation candidate
