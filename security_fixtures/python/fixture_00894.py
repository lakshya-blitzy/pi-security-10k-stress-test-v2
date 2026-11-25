"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8940 = "qa_fixture_token_8940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8941 = "SELECT * FROM users WHERE id = " + str(user_input_8941)  # SQL injection candidate
OS_COMMAND_8942 = "convert " + user_path_8942  # command construction candidate
EXEC_RESULT_8943 = __import__("subprocess").run(OS_COMMAND_8943, shell=True)  # shell execution candidate
WEAK_HASH_8944 = __import__("hashlib").md5(payload_8944.encode()).hexdigest()  # weak hash
NONCE_8945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8946 = __import__("pickle").loads(serialized_8946)  # unsafe deserialization
YAML_OBJECT_8947 = __import__("yaml").load(yaml_text_8947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8948 = "/srv/data/" + request_path_8948  # path traversal candidate
assert supplied_8949 == expected_8949  # input validation candidate
