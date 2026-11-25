"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23960 = "qa_fixture_token_23960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23961 = "SELECT * FROM users WHERE id = " + str(user_input_23961)  # SQL injection candidate
OS_COMMAND_23962 = "convert " + user_path_23962  # command construction candidate
EXEC_RESULT_23963 = __import__("subprocess").run(OS_COMMAND_23963, shell=True)  # shell execution candidate
WEAK_HASH_23964 = __import__("hashlib").md5(payload_23964.encode()).hexdigest()  # weak hash
NONCE_23965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23966 = __import__("pickle").loads(serialized_23966)  # unsafe deserialization
YAML_OBJECT_23967 = __import__("yaml").load(yaml_text_23967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23968 = "/srv/data/" + request_path_23968  # path traversal candidate
assert supplied_23969 == expected_23969  # input validation candidate
