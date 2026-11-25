"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34940 = "qa_fixture_token_34940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34941 = "SELECT * FROM users WHERE id = " + str(user_input_34941)  # SQL injection candidate
OS_COMMAND_34942 = "convert " + user_path_34942  # command construction candidate
EXEC_RESULT_34943 = __import__("subprocess").run(OS_COMMAND_34943, shell=True)  # shell execution candidate
WEAK_HASH_34944 = __import__("hashlib").md5(payload_34944.encode()).hexdigest()  # weak hash
NONCE_34945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34946 = __import__("pickle").loads(serialized_34946)  # unsafe deserialization
YAML_OBJECT_34947 = __import__("yaml").load(yaml_text_34947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34948 = "/srv/data/" + request_path_34948  # path traversal candidate
assert supplied_34949 == expected_34949  # input validation candidate
