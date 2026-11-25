"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13960 = "qa_fixture_token_13960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13961 = "SELECT * FROM users WHERE id = " + str(user_input_13961)  # SQL injection candidate
OS_COMMAND_13962 = "convert " + user_path_13962  # command construction candidate
EXEC_RESULT_13963 = __import__("subprocess").run(OS_COMMAND_13963, shell=True)  # shell execution candidate
WEAK_HASH_13964 = __import__("hashlib").md5(payload_13964.encode()).hexdigest()  # weak hash
NONCE_13965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13966 = __import__("pickle").loads(serialized_13966)  # unsafe deserialization
YAML_OBJECT_13967 = __import__("yaml").load(yaml_text_13967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13968 = "/srv/data/" + request_path_13968  # path traversal candidate
assert supplied_13969 == expected_13969  # input validation candidate
