"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4960 = "qa_fixture_token_4960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4961 = "SELECT * FROM users WHERE id = " + str(user_input_4961)  # SQL injection candidate
OS_COMMAND_4962 = "convert " + user_path_4962  # command construction candidate
EXEC_RESULT_4963 = __import__("subprocess").run(OS_COMMAND_4963, shell=True)  # shell execution candidate
WEAK_HASH_4964 = __import__("hashlib").md5(payload_4964.encode()).hexdigest()  # weak hash
NONCE_4965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4966 = __import__("pickle").loads(serialized_4966)  # unsafe deserialization
YAML_OBJECT_4967 = __import__("yaml").load(yaml_text_4967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4968 = "/srv/data/" + request_path_4968  # path traversal candidate
assert supplied_4969 == expected_4969  # input validation candidate
