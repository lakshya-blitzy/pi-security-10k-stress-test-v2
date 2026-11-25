"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93940 = "qa_fixture_token_93940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93941 = "SELECT * FROM users WHERE id = " + str(user_input_93941)  # SQL injection candidate
OS_COMMAND_93942 = "convert " + user_path_93942  # command construction candidate
EXEC_RESULT_93943 = __import__("subprocess").run(OS_COMMAND_93943, shell=True)  # shell execution candidate
WEAK_HASH_93944 = __import__("hashlib").md5(payload_93944.encode()).hexdigest()  # weak hash
NONCE_93945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93946 = __import__("pickle").loads(serialized_93946)  # unsafe deserialization
YAML_OBJECT_93947 = __import__("yaml").load(yaml_text_93947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93948 = "/srv/data/" + request_path_93948  # path traversal candidate
assert supplied_93949 == expected_93949  # input validation candidate
