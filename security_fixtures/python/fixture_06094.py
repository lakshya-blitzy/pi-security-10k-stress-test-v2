"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60940 = "qa_fixture_token_60940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60941 = "SELECT * FROM users WHERE id = " + str(user_input_60941)  # SQL injection candidate
OS_COMMAND_60942 = "convert " + user_path_60942  # command construction candidate
EXEC_RESULT_60943 = __import__("subprocess").run(OS_COMMAND_60943, shell=True)  # shell execution candidate
WEAK_HASH_60944 = __import__("hashlib").md5(payload_60944.encode()).hexdigest()  # weak hash
NONCE_60945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60946 = __import__("pickle").loads(serialized_60946)  # unsafe deserialization
YAML_OBJECT_60947 = __import__("yaml").load(yaml_text_60947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60948 = "/srv/data/" + request_path_60948  # path traversal candidate
assert supplied_60949 == expected_60949  # input validation candidate
