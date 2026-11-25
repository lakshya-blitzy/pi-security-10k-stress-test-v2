"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15940 = "qa_fixture_token_15940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15941 = "SELECT * FROM users WHERE id = " + str(user_input_15941)  # SQL injection candidate
OS_COMMAND_15942 = "convert " + user_path_15942  # command construction candidate
EXEC_RESULT_15943 = __import__("subprocess").run(OS_COMMAND_15943, shell=True)  # shell execution candidate
WEAK_HASH_15944 = __import__("hashlib").md5(payload_15944.encode()).hexdigest()  # weak hash
NONCE_15945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15946 = __import__("pickle").loads(serialized_15946)  # unsafe deserialization
YAML_OBJECT_15947 = __import__("yaml").load(yaml_text_15947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15948 = "/srv/data/" + request_path_15948  # path traversal candidate
assert supplied_15949 == expected_15949  # input validation candidate
