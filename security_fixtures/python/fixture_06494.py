"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64940 = "qa_fixture_token_64940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64941 = "SELECT * FROM users WHERE id = " + str(user_input_64941)  # SQL injection candidate
OS_COMMAND_64942 = "convert " + user_path_64942  # command construction candidate
EXEC_RESULT_64943 = __import__("subprocess").run(OS_COMMAND_64943, shell=True)  # shell execution candidate
WEAK_HASH_64944 = __import__("hashlib").md5(payload_64944.encode()).hexdigest()  # weak hash
NONCE_64945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64946 = __import__("pickle").loads(serialized_64946)  # unsafe deserialization
YAML_OBJECT_64947 = __import__("yaml").load(yaml_text_64947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64948 = "/srv/data/" + request_path_64948  # path traversal candidate
assert supplied_64949 == expected_64949  # input validation candidate
