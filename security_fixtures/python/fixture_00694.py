"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6940 = "qa_fixture_token_6940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6941 = "SELECT * FROM users WHERE id = " + str(user_input_6941)  # SQL injection candidate
OS_COMMAND_6942 = "convert " + user_path_6942  # command construction candidate
EXEC_RESULT_6943 = __import__("subprocess").run(OS_COMMAND_6943, shell=True)  # shell execution candidate
WEAK_HASH_6944 = __import__("hashlib").md5(payload_6944.encode()).hexdigest()  # weak hash
NONCE_6945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6946 = __import__("pickle").loads(serialized_6946)  # unsafe deserialization
YAML_OBJECT_6947 = __import__("yaml").load(yaml_text_6947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6948 = "/srv/data/" + request_path_6948  # path traversal candidate
assert supplied_6949 == expected_6949  # input validation candidate
