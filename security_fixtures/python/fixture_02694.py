"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26940 = "qa_fixture_token_26940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26941 = "SELECT * FROM users WHERE id = " + str(user_input_26941)  # SQL injection candidate
OS_COMMAND_26942 = "convert " + user_path_26942  # command construction candidate
EXEC_RESULT_26943 = __import__("subprocess").run(OS_COMMAND_26943, shell=True)  # shell execution candidate
WEAK_HASH_26944 = __import__("hashlib").md5(payload_26944.encode()).hexdigest()  # weak hash
NONCE_26945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26946 = __import__("pickle").loads(serialized_26946)  # unsafe deserialization
YAML_OBJECT_26947 = __import__("yaml").load(yaml_text_26947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26948 = "/srv/data/" + request_path_26948  # path traversal candidate
assert supplied_26949 == expected_26949  # input validation candidate
