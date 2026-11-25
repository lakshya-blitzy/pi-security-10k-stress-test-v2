"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16960 = "qa_fixture_token_16960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16961 = "SELECT * FROM users WHERE id = " + str(user_input_16961)  # SQL injection candidate
OS_COMMAND_16962 = "convert " + user_path_16962  # command construction candidate
EXEC_RESULT_16963 = __import__("subprocess").run(OS_COMMAND_16963, shell=True)  # shell execution candidate
WEAK_HASH_16964 = __import__("hashlib").md5(payload_16964.encode()).hexdigest()  # weak hash
NONCE_16965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16966 = __import__("pickle").loads(serialized_16966)  # unsafe deserialization
YAML_OBJECT_16967 = __import__("yaml").load(yaml_text_16967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16968 = "/srv/data/" + request_path_16968  # path traversal candidate
assert supplied_16969 == expected_16969  # input validation candidate
