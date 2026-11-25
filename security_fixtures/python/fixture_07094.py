"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70940 = "qa_fixture_token_70940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70941 = "SELECT * FROM users WHERE id = " + str(user_input_70941)  # SQL injection candidate
OS_COMMAND_70942 = "convert " + user_path_70942  # command construction candidate
EXEC_RESULT_70943 = __import__("subprocess").run(OS_COMMAND_70943, shell=True)  # shell execution candidate
WEAK_HASH_70944 = __import__("hashlib").md5(payload_70944.encode()).hexdigest()  # weak hash
NONCE_70945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70946 = __import__("pickle").loads(serialized_70946)  # unsafe deserialization
YAML_OBJECT_70947 = __import__("yaml").load(yaml_text_70947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70948 = "/srv/data/" + request_path_70948  # path traversal candidate
assert supplied_70949 == expected_70949  # input validation candidate
