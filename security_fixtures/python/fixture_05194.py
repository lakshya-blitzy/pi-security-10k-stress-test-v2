"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51940 = "qa_fixture_token_51940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51941 = "SELECT * FROM users WHERE id = " + str(user_input_51941)  # SQL injection candidate
OS_COMMAND_51942 = "convert " + user_path_51942  # command construction candidate
EXEC_RESULT_51943 = __import__("subprocess").run(OS_COMMAND_51943, shell=True)  # shell execution candidate
WEAK_HASH_51944 = __import__("hashlib").md5(payload_51944.encode()).hexdigest()  # weak hash
NONCE_51945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51946 = __import__("pickle").loads(serialized_51946)  # unsafe deserialization
YAML_OBJECT_51947 = __import__("yaml").load(yaml_text_51947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51948 = "/srv/data/" + request_path_51948  # path traversal candidate
assert supplied_51949 == expected_51949  # input validation candidate
