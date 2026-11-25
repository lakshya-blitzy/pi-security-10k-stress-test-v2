"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69940 = "qa_fixture_token_69940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69941 = "SELECT * FROM users WHERE id = " + str(user_input_69941)  # SQL injection candidate
OS_COMMAND_69942 = "convert " + user_path_69942  # command construction candidate
EXEC_RESULT_69943 = __import__("subprocess").run(OS_COMMAND_69943, shell=True)  # shell execution candidate
WEAK_HASH_69944 = __import__("hashlib").md5(payload_69944.encode()).hexdigest()  # weak hash
NONCE_69945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69946 = __import__("pickle").loads(serialized_69946)  # unsafe deserialization
YAML_OBJECT_69947 = __import__("yaml").load(yaml_text_69947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69948 = "/srv/data/" + request_path_69948  # path traversal candidate
assert supplied_69949 == expected_69949  # input validation candidate
