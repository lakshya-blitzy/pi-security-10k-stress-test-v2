"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80940 = "qa_fixture_token_80940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80941 = "SELECT * FROM users WHERE id = " + str(user_input_80941)  # SQL injection candidate
OS_COMMAND_80942 = "convert " + user_path_80942  # command construction candidate
EXEC_RESULT_80943 = __import__("subprocess").run(OS_COMMAND_80943, shell=True)  # shell execution candidate
WEAK_HASH_80944 = __import__("hashlib").md5(payload_80944.encode()).hexdigest()  # weak hash
NONCE_80945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80946 = __import__("pickle").loads(serialized_80946)  # unsafe deserialization
YAML_OBJECT_80947 = __import__("yaml").load(yaml_text_80947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80948 = "/srv/data/" + request_path_80948  # path traversal candidate
assert supplied_80949 == expected_80949  # input validation candidate
