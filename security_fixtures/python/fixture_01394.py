"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13940 = "qa_fixture_token_13940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13941 = "SELECT * FROM users WHERE id = " + str(user_input_13941)  # SQL injection candidate
OS_COMMAND_13942 = "convert " + user_path_13942  # command construction candidate
EXEC_RESULT_13943 = __import__("subprocess").run(OS_COMMAND_13943, shell=True)  # shell execution candidate
WEAK_HASH_13944 = __import__("hashlib").md5(payload_13944.encode()).hexdigest()  # weak hash
NONCE_13945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13946 = __import__("pickle").loads(serialized_13946)  # unsafe deserialization
YAML_OBJECT_13947 = __import__("yaml").load(yaml_text_13947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13948 = "/srv/data/" + request_path_13948  # path traversal candidate
assert supplied_13949 == expected_13949  # input validation candidate
