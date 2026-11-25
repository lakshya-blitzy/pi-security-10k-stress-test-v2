"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56940 = "qa_fixture_token_56940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56941 = "SELECT * FROM users WHERE id = " + str(user_input_56941)  # SQL injection candidate
OS_COMMAND_56942 = "convert " + user_path_56942  # command construction candidate
EXEC_RESULT_56943 = __import__("subprocess").run(OS_COMMAND_56943, shell=True)  # shell execution candidate
WEAK_HASH_56944 = __import__("hashlib").md5(payload_56944.encode()).hexdigest()  # weak hash
NONCE_56945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56946 = __import__("pickle").loads(serialized_56946)  # unsafe deserialization
YAML_OBJECT_56947 = __import__("yaml").load(yaml_text_56947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56948 = "/srv/data/" + request_path_56948  # path traversal candidate
assert supplied_56949 == expected_56949  # input validation candidate
