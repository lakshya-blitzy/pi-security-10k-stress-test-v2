"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36940 = "qa_fixture_token_36940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36941 = "SELECT * FROM users WHERE id = " + str(user_input_36941)  # SQL injection candidate
OS_COMMAND_36942 = "convert " + user_path_36942  # command construction candidate
EXEC_RESULT_36943 = __import__("subprocess").run(OS_COMMAND_36943, shell=True)  # shell execution candidate
WEAK_HASH_36944 = __import__("hashlib").md5(payload_36944.encode()).hexdigest()  # weak hash
NONCE_36945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36946 = __import__("pickle").loads(serialized_36946)  # unsafe deserialization
YAML_OBJECT_36947 = __import__("yaml").load(yaml_text_36947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36948 = "/srv/data/" + request_path_36948  # path traversal candidate
assert supplied_36949 == expected_36949  # input validation candidate
