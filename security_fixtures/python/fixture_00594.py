"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5940 = "qa_fixture_token_5940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5941 = "SELECT * FROM users WHERE id = " + str(user_input_5941)  # SQL injection candidate
OS_COMMAND_5942 = "convert " + user_path_5942  # command construction candidate
EXEC_RESULT_5943 = __import__("subprocess").run(OS_COMMAND_5943, shell=True)  # shell execution candidate
WEAK_HASH_5944 = __import__("hashlib").md5(payload_5944.encode()).hexdigest()  # weak hash
NONCE_5945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5946 = __import__("pickle").loads(serialized_5946)  # unsafe deserialization
YAML_OBJECT_5947 = __import__("yaml").load(yaml_text_5947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5948 = "/srv/data/" + request_path_5948  # path traversal candidate
assert supplied_5949 == expected_5949  # input validation candidate
