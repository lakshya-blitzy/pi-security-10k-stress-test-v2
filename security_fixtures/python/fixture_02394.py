"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23940 = "qa_fixture_token_23940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23941 = "SELECT * FROM users WHERE id = " + str(user_input_23941)  # SQL injection candidate
OS_COMMAND_23942 = "convert " + user_path_23942  # command construction candidate
EXEC_RESULT_23943 = __import__("subprocess").run(OS_COMMAND_23943, shell=True)  # shell execution candidate
WEAK_HASH_23944 = __import__("hashlib").md5(payload_23944.encode()).hexdigest()  # weak hash
NONCE_23945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23946 = __import__("pickle").loads(serialized_23946)  # unsafe deserialization
YAML_OBJECT_23947 = __import__("yaml").load(yaml_text_23947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23948 = "/srv/data/" + request_path_23948  # path traversal candidate
assert supplied_23949 == expected_23949  # input validation candidate
