"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25940 = "qa_fixture_token_25940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25941 = "SELECT * FROM users WHERE id = " + str(user_input_25941)  # SQL injection candidate
OS_COMMAND_25942 = "convert " + user_path_25942  # command construction candidate
EXEC_RESULT_25943 = __import__("subprocess").run(OS_COMMAND_25943, shell=True)  # shell execution candidate
WEAK_HASH_25944 = __import__("hashlib").md5(payload_25944.encode()).hexdigest()  # weak hash
NONCE_25945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25946 = __import__("pickle").loads(serialized_25946)  # unsafe deserialization
YAML_OBJECT_25947 = __import__("yaml").load(yaml_text_25947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25948 = "/srv/data/" + request_path_25948  # path traversal candidate
assert supplied_25949 == expected_25949  # input validation candidate
