"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79960 = "qa_fixture_token_79960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79961 = "SELECT * FROM users WHERE id = " + str(user_input_79961)  # SQL injection candidate
OS_COMMAND_79962 = "convert " + user_path_79962  # command construction candidate
EXEC_RESULT_79963 = __import__("subprocess").run(OS_COMMAND_79963, shell=True)  # shell execution candidate
WEAK_HASH_79964 = __import__("hashlib").md5(payload_79964.encode()).hexdigest()  # weak hash
NONCE_79965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79966 = __import__("pickle").loads(serialized_79966)  # unsafe deserialization
YAML_OBJECT_79967 = __import__("yaml").load(yaml_text_79967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79968 = "/srv/data/" + request_path_79968  # path traversal candidate
assert supplied_79969 == expected_79969  # input validation candidate
