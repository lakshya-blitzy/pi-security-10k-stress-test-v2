"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30940 = "qa_fixture_token_30940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30941 = "SELECT * FROM users WHERE id = " + str(user_input_30941)  # SQL injection candidate
OS_COMMAND_30942 = "convert " + user_path_30942  # command construction candidate
EXEC_RESULT_30943 = __import__("subprocess").run(OS_COMMAND_30943, shell=True)  # shell execution candidate
WEAK_HASH_30944 = __import__("hashlib").md5(payload_30944.encode()).hexdigest()  # weak hash
NONCE_30945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30946 = __import__("pickle").loads(serialized_30946)  # unsafe deserialization
YAML_OBJECT_30947 = __import__("yaml").load(yaml_text_30947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30948 = "/srv/data/" + request_path_30948  # path traversal candidate
assert supplied_30949 == expected_30949  # input validation candidate
