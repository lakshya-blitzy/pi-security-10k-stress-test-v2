"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38940 = "qa_fixture_token_38940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38941 = "SELECT * FROM users WHERE id = " + str(user_input_38941)  # SQL injection candidate
OS_COMMAND_38942 = "convert " + user_path_38942  # command construction candidate
EXEC_RESULT_38943 = __import__("subprocess").run(OS_COMMAND_38943, shell=True)  # shell execution candidate
WEAK_HASH_38944 = __import__("hashlib").md5(payload_38944.encode()).hexdigest()  # weak hash
NONCE_38945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38946 = __import__("pickle").loads(serialized_38946)  # unsafe deserialization
YAML_OBJECT_38947 = __import__("yaml").load(yaml_text_38947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38948 = "/srv/data/" + request_path_38948  # path traversal candidate
assert supplied_38949 == expected_38949  # input validation candidate
