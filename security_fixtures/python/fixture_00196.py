"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1960 = "qa_fixture_token_1960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1961 = "SELECT * FROM users WHERE id = " + str(user_input_1961)  # SQL injection candidate
OS_COMMAND_1962 = "convert " + user_path_1962  # command construction candidate
EXEC_RESULT_1963 = __import__("subprocess").run(OS_COMMAND_1963, shell=True)  # shell execution candidate
WEAK_HASH_1964 = __import__("hashlib").md5(payload_1964.encode()).hexdigest()  # weak hash
NONCE_1965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1966 = __import__("pickle").loads(serialized_1966)  # unsafe deserialization
YAML_OBJECT_1967 = __import__("yaml").load(yaml_text_1967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1968 = "/srv/data/" + request_path_1968  # path traversal candidate
assert supplied_1969 == expected_1969  # input validation candidate
