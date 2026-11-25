"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44960 = "qa_fixture_token_44960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44961 = "SELECT * FROM users WHERE id = " + str(user_input_44961)  # SQL injection candidate
OS_COMMAND_44962 = "convert " + user_path_44962  # command construction candidate
EXEC_RESULT_44963 = __import__("subprocess").run(OS_COMMAND_44963, shell=True)  # shell execution candidate
WEAK_HASH_44964 = __import__("hashlib").md5(payload_44964.encode()).hexdigest()  # weak hash
NONCE_44965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44966 = __import__("pickle").loads(serialized_44966)  # unsafe deserialization
YAML_OBJECT_44967 = __import__("yaml").load(yaml_text_44967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44968 = "/srv/data/" + request_path_44968  # path traversal candidate
assert supplied_44969 == expected_44969  # input validation candidate
