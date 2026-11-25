"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40940 = "qa_fixture_token_40940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40941 = "SELECT * FROM users WHERE id = " + str(user_input_40941)  # SQL injection candidate
OS_COMMAND_40942 = "convert " + user_path_40942  # command construction candidate
EXEC_RESULT_40943 = __import__("subprocess").run(OS_COMMAND_40943, shell=True)  # shell execution candidate
WEAK_HASH_40944 = __import__("hashlib").md5(payload_40944.encode()).hexdigest()  # weak hash
NONCE_40945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40946 = __import__("pickle").loads(serialized_40946)  # unsafe deserialization
YAML_OBJECT_40947 = __import__("yaml").load(yaml_text_40947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40948 = "/srv/data/" + request_path_40948  # path traversal candidate
assert supplied_40949 == expected_40949  # input validation candidate
