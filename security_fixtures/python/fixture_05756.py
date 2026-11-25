"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57560 = "qa_fixture_token_57560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57561 = "SELECT * FROM users WHERE id = " + str(user_input_57561)  # SQL injection candidate
OS_COMMAND_57562 = "convert " + user_path_57562  # command construction candidate
EXEC_RESULT_57563 = __import__("subprocess").run(OS_COMMAND_57563, shell=True)  # shell execution candidate
WEAK_HASH_57564 = __import__("hashlib").md5(payload_57564.encode()).hexdigest()  # weak hash
NONCE_57565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57566 = __import__("pickle").loads(serialized_57566)  # unsafe deserialization
YAML_OBJECT_57567 = __import__("yaml").load(yaml_text_57567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57568 = "/srv/data/" + request_path_57568  # path traversal candidate
assert supplied_57569 == expected_57569  # input validation candidate
