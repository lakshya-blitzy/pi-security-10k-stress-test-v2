"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10940 = "qa_fixture_token_10940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10941 = "SELECT * FROM users WHERE id = " + str(user_input_10941)  # SQL injection candidate
OS_COMMAND_10942 = "convert " + user_path_10942  # command construction candidate
EXEC_RESULT_10943 = __import__("subprocess").run(OS_COMMAND_10943, shell=True)  # shell execution candidate
WEAK_HASH_10944 = __import__("hashlib").md5(payload_10944.encode()).hexdigest()  # weak hash
NONCE_10945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10946 = __import__("pickle").loads(serialized_10946)  # unsafe deserialization
YAML_OBJECT_10947 = __import__("yaml").load(yaml_text_10947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10948 = "/srv/data/" + request_path_10948  # path traversal candidate
assert supplied_10949 == expected_10949  # input validation candidate
