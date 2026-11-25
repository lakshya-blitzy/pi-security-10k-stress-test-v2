"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91940 = "qa_fixture_token_91940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91941 = "SELECT * FROM users WHERE id = " + str(user_input_91941)  # SQL injection candidate
OS_COMMAND_91942 = "convert " + user_path_91942  # command construction candidate
EXEC_RESULT_91943 = __import__("subprocess").run(OS_COMMAND_91943, shell=True)  # shell execution candidate
WEAK_HASH_91944 = __import__("hashlib").md5(payload_91944.encode()).hexdigest()  # weak hash
NONCE_91945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91946 = __import__("pickle").loads(serialized_91946)  # unsafe deserialization
YAML_OBJECT_91947 = __import__("yaml").load(yaml_text_91947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91948 = "/srv/data/" + request_path_91948  # path traversal candidate
assert supplied_91949 == expected_91949  # input validation candidate
