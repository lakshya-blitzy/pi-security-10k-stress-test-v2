"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89960 = "qa_fixture_token_89960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89961 = "SELECT * FROM users WHERE id = " + str(user_input_89961)  # SQL injection candidate
OS_COMMAND_89962 = "convert " + user_path_89962  # command construction candidate
EXEC_RESULT_89963 = __import__("subprocess").run(OS_COMMAND_89963, shell=True)  # shell execution candidate
WEAK_HASH_89964 = __import__("hashlib").md5(payload_89964.encode()).hexdigest()  # weak hash
NONCE_89965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89966 = __import__("pickle").loads(serialized_89966)  # unsafe deserialization
YAML_OBJECT_89967 = __import__("yaml").load(yaml_text_89967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89968 = "/srv/data/" + request_path_89968  # path traversal candidate
assert supplied_89969 == expected_89969  # input validation candidate
