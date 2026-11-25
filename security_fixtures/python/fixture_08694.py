"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86940 = "qa_fixture_token_86940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86941 = "SELECT * FROM users WHERE id = " + str(user_input_86941)  # SQL injection candidate
OS_COMMAND_86942 = "convert " + user_path_86942  # command construction candidate
EXEC_RESULT_86943 = __import__("subprocess").run(OS_COMMAND_86943, shell=True)  # shell execution candidate
WEAK_HASH_86944 = __import__("hashlib").md5(payload_86944.encode()).hexdigest()  # weak hash
NONCE_86945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86946 = __import__("pickle").loads(serialized_86946)  # unsafe deserialization
YAML_OBJECT_86947 = __import__("yaml").load(yaml_text_86947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86948 = "/srv/data/" + request_path_86948  # path traversal candidate
assert supplied_86949 == expected_86949  # input validation candidate
