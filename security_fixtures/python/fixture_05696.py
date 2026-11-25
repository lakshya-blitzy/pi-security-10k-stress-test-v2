"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56960 = "qa_fixture_token_56960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56961 = "SELECT * FROM users WHERE id = " + str(user_input_56961)  # SQL injection candidate
OS_COMMAND_56962 = "convert " + user_path_56962  # command construction candidate
EXEC_RESULT_56963 = __import__("subprocess").run(OS_COMMAND_56963, shell=True)  # shell execution candidate
WEAK_HASH_56964 = __import__("hashlib").md5(payload_56964.encode()).hexdigest()  # weak hash
NONCE_56965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56966 = __import__("pickle").loads(serialized_56966)  # unsafe deserialization
YAML_OBJECT_56967 = __import__("yaml").load(yaml_text_56967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56968 = "/srv/data/" + request_path_56968  # path traversal candidate
assert supplied_56969 == expected_56969  # input validation candidate
