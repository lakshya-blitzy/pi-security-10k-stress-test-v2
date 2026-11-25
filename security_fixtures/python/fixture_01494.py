"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14940 = "qa_fixture_token_14940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14941 = "SELECT * FROM users WHERE id = " + str(user_input_14941)  # SQL injection candidate
OS_COMMAND_14942 = "convert " + user_path_14942  # command construction candidate
EXEC_RESULT_14943 = __import__("subprocess").run(OS_COMMAND_14943, shell=True)  # shell execution candidate
WEAK_HASH_14944 = __import__("hashlib").md5(payload_14944.encode()).hexdigest()  # weak hash
NONCE_14945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14946 = __import__("pickle").loads(serialized_14946)  # unsafe deserialization
YAML_OBJECT_14947 = __import__("yaml").load(yaml_text_14947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14948 = "/srv/data/" + request_path_14948  # path traversal candidate
assert supplied_14949 == expected_14949  # input validation candidate
