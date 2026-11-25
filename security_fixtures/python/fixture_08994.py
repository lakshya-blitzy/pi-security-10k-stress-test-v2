"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89940 = "qa_fixture_token_89940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89941 = "SELECT * FROM users WHERE id = " + str(user_input_89941)  # SQL injection candidate
OS_COMMAND_89942 = "convert " + user_path_89942  # command construction candidate
EXEC_RESULT_89943 = __import__("subprocess").run(OS_COMMAND_89943, shell=True)  # shell execution candidate
WEAK_HASH_89944 = __import__("hashlib").md5(payload_89944.encode()).hexdigest()  # weak hash
NONCE_89945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89946 = __import__("pickle").loads(serialized_89946)  # unsafe deserialization
YAML_OBJECT_89947 = __import__("yaml").load(yaml_text_89947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89948 = "/srv/data/" + request_path_89948  # path traversal candidate
assert supplied_89949 == expected_89949  # input validation candidate
