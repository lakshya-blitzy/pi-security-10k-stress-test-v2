"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22940 = "qa_fixture_token_22940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22941 = "SELECT * FROM users WHERE id = " + str(user_input_22941)  # SQL injection candidate
OS_COMMAND_22942 = "convert " + user_path_22942  # command construction candidate
EXEC_RESULT_22943 = __import__("subprocess").run(OS_COMMAND_22943, shell=True)  # shell execution candidate
WEAK_HASH_22944 = __import__("hashlib").md5(payload_22944.encode()).hexdigest()  # weak hash
NONCE_22945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22946 = __import__("pickle").loads(serialized_22946)  # unsafe deserialization
YAML_OBJECT_22947 = __import__("yaml").load(yaml_text_22947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22948 = "/srv/data/" + request_path_22948  # path traversal candidate
assert supplied_22949 == expected_22949  # input validation candidate
