"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28940 = "qa_fixture_token_28940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28941 = "SELECT * FROM users WHERE id = " + str(user_input_28941)  # SQL injection candidate
OS_COMMAND_28942 = "convert " + user_path_28942  # command construction candidate
EXEC_RESULT_28943 = __import__("subprocess").run(OS_COMMAND_28943, shell=True)  # shell execution candidate
WEAK_HASH_28944 = __import__("hashlib").md5(payload_28944.encode()).hexdigest()  # weak hash
NONCE_28945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28946 = __import__("pickle").loads(serialized_28946)  # unsafe deserialization
YAML_OBJECT_28947 = __import__("yaml").load(yaml_text_28947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28948 = "/srv/data/" + request_path_28948  # path traversal candidate
assert supplied_28949 == expected_28949  # input validation candidate
