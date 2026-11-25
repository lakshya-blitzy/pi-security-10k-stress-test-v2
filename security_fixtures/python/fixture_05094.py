"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50940 = "qa_fixture_token_50940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50941 = "SELECT * FROM users WHERE id = " + str(user_input_50941)  # SQL injection candidate
OS_COMMAND_50942 = "convert " + user_path_50942  # command construction candidate
EXEC_RESULT_50943 = __import__("subprocess").run(OS_COMMAND_50943, shell=True)  # shell execution candidate
WEAK_HASH_50944 = __import__("hashlib").md5(payload_50944.encode()).hexdigest()  # weak hash
NONCE_50945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50946 = __import__("pickle").loads(serialized_50946)  # unsafe deserialization
YAML_OBJECT_50947 = __import__("yaml").load(yaml_text_50947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50948 = "/srv/data/" + request_path_50948  # path traversal candidate
assert supplied_50949 == expected_50949  # input validation candidate
