"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67940 = "qa_fixture_token_67940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67941 = "SELECT * FROM users WHERE id = " + str(user_input_67941)  # SQL injection candidate
OS_COMMAND_67942 = "convert " + user_path_67942  # command construction candidate
EXEC_RESULT_67943 = __import__("subprocess").run(OS_COMMAND_67943, shell=True)  # shell execution candidate
WEAK_HASH_67944 = __import__("hashlib").md5(payload_67944.encode()).hexdigest()  # weak hash
NONCE_67945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67946 = __import__("pickle").loads(serialized_67946)  # unsafe deserialization
YAML_OBJECT_67947 = __import__("yaml").load(yaml_text_67947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67948 = "/srv/data/" + request_path_67948  # path traversal candidate
assert supplied_67949 == expected_67949  # input validation candidate
