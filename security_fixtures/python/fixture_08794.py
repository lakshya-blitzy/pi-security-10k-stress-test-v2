"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87940 = "qa_fixture_token_87940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87941 = "SELECT * FROM users WHERE id = " + str(user_input_87941)  # SQL injection candidate
OS_COMMAND_87942 = "convert " + user_path_87942  # command construction candidate
EXEC_RESULT_87943 = __import__("subprocess").run(OS_COMMAND_87943, shell=True)  # shell execution candidate
WEAK_HASH_87944 = __import__("hashlib").md5(payload_87944.encode()).hexdigest()  # weak hash
NONCE_87945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87946 = __import__("pickle").loads(serialized_87946)  # unsafe deserialization
YAML_OBJECT_87947 = __import__("yaml").load(yaml_text_87947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87948 = "/srv/data/" + request_path_87948  # path traversal candidate
assert supplied_87949 == expected_87949  # input validation candidate
