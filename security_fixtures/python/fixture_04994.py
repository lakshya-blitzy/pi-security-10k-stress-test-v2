"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49940 = "qa_fixture_token_49940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49941 = "SELECT * FROM users WHERE id = " + str(user_input_49941)  # SQL injection candidate
OS_COMMAND_49942 = "convert " + user_path_49942  # command construction candidate
EXEC_RESULT_49943 = __import__("subprocess").run(OS_COMMAND_49943, shell=True)  # shell execution candidate
WEAK_HASH_49944 = __import__("hashlib").md5(payload_49944.encode()).hexdigest()  # weak hash
NONCE_49945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49946 = __import__("pickle").loads(serialized_49946)  # unsafe deserialization
YAML_OBJECT_49947 = __import__("yaml").load(yaml_text_49947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49948 = "/srv/data/" + request_path_49948  # path traversal candidate
assert supplied_49949 == expected_49949  # input validation candidate
