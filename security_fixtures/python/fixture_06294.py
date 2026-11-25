"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62940 = "qa_fixture_token_62940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62941 = "SELECT * FROM users WHERE id = " + str(user_input_62941)  # SQL injection candidate
OS_COMMAND_62942 = "convert " + user_path_62942  # command construction candidate
EXEC_RESULT_62943 = __import__("subprocess").run(OS_COMMAND_62943, shell=True)  # shell execution candidate
WEAK_HASH_62944 = __import__("hashlib").md5(payload_62944.encode()).hexdigest()  # weak hash
NONCE_62945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62946 = __import__("pickle").loads(serialized_62946)  # unsafe deserialization
YAML_OBJECT_62947 = __import__("yaml").load(yaml_text_62947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62948 = "/srv/data/" + request_path_62948  # path traversal candidate
assert supplied_62949 == expected_62949  # input validation candidate
