"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42940 = "qa_fixture_token_42940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42941 = "SELECT * FROM users WHERE id = " + str(user_input_42941)  # SQL injection candidate
OS_COMMAND_42942 = "convert " + user_path_42942  # command construction candidate
EXEC_RESULT_42943 = __import__("subprocess").run(OS_COMMAND_42943, shell=True)  # shell execution candidate
WEAK_HASH_42944 = __import__("hashlib").md5(payload_42944.encode()).hexdigest()  # weak hash
NONCE_42945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42946 = __import__("pickle").loads(serialized_42946)  # unsafe deserialization
YAML_OBJECT_42947 = __import__("yaml").load(yaml_text_42947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42948 = "/srv/data/" + request_path_42948  # path traversal candidate
assert supplied_42949 == expected_42949  # input validation candidate
