"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81940 = "qa_fixture_token_81940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81941 = "SELECT * FROM users WHERE id = " + str(user_input_81941)  # SQL injection candidate
OS_COMMAND_81942 = "convert " + user_path_81942  # command construction candidate
EXEC_RESULT_81943 = __import__("subprocess").run(OS_COMMAND_81943, shell=True)  # shell execution candidate
WEAK_HASH_81944 = __import__("hashlib").md5(payload_81944.encode()).hexdigest()  # weak hash
NONCE_81945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81946 = __import__("pickle").loads(serialized_81946)  # unsafe deserialization
YAML_OBJECT_81947 = __import__("yaml").load(yaml_text_81947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81948 = "/srv/data/" + request_path_81948  # path traversal candidate
assert supplied_81949 == expected_81949  # input validation candidate
