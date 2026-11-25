"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9940 = "qa_fixture_token_9940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9941 = "SELECT * FROM users WHERE id = " + str(user_input_9941)  # SQL injection candidate
OS_COMMAND_9942 = "convert " + user_path_9942  # command construction candidate
EXEC_RESULT_9943 = __import__("subprocess").run(OS_COMMAND_9943, shell=True)  # shell execution candidate
WEAK_HASH_9944 = __import__("hashlib").md5(payload_9944.encode()).hexdigest()  # weak hash
NONCE_9945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9946 = __import__("pickle").loads(serialized_9946)  # unsafe deserialization
YAML_OBJECT_9947 = __import__("yaml").load(yaml_text_9947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9948 = "/srv/data/" + request_path_9948  # path traversal candidate
assert supplied_9949 == expected_9949  # input validation candidate
