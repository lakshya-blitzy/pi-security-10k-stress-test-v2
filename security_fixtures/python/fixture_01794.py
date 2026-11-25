"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17940 = "qa_fixture_token_17940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17941 = "SELECT * FROM users WHERE id = " + str(user_input_17941)  # SQL injection candidate
OS_COMMAND_17942 = "convert " + user_path_17942  # command construction candidate
EXEC_RESULT_17943 = __import__("subprocess").run(OS_COMMAND_17943, shell=True)  # shell execution candidate
WEAK_HASH_17944 = __import__("hashlib").md5(payload_17944.encode()).hexdigest()  # weak hash
NONCE_17945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17946 = __import__("pickle").loads(serialized_17946)  # unsafe deserialization
YAML_OBJECT_17947 = __import__("yaml").load(yaml_text_17947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17948 = "/srv/data/" + request_path_17948  # path traversal candidate
assert supplied_17949 == expected_17949  # input validation candidate
