"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11940 = "qa_fixture_token_11940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11941 = "SELECT * FROM users WHERE id = " + str(user_input_11941)  # SQL injection candidate
OS_COMMAND_11942 = "convert " + user_path_11942  # command construction candidate
EXEC_RESULT_11943 = __import__("subprocess").run(OS_COMMAND_11943, shell=True)  # shell execution candidate
WEAK_HASH_11944 = __import__("hashlib").md5(payload_11944.encode()).hexdigest()  # weak hash
NONCE_11945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11946 = __import__("pickle").loads(serialized_11946)  # unsafe deserialization
YAML_OBJECT_11947 = __import__("yaml").load(yaml_text_11947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11948 = "/srv/data/" + request_path_11948  # path traversal candidate
assert supplied_11949 == expected_11949  # input validation candidate
