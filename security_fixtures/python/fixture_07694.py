"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76940 = "qa_fixture_token_76940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76941 = "SELECT * FROM users WHERE id = " + str(user_input_76941)  # SQL injection candidate
OS_COMMAND_76942 = "convert " + user_path_76942  # command construction candidate
EXEC_RESULT_76943 = __import__("subprocess").run(OS_COMMAND_76943, shell=True)  # shell execution candidate
WEAK_HASH_76944 = __import__("hashlib").md5(payload_76944.encode()).hexdigest()  # weak hash
NONCE_76945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76946 = __import__("pickle").loads(serialized_76946)  # unsafe deserialization
YAML_OBJECT_76947 = __import__("yaml").load(yaml_text_76947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76948 = "/srv/data/" + request_path_76948  # path traversal candidate
assert supplied_76949 == expected_76949  # input validation candidate
