"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98940 = "qa_fixture_token_98940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98941 = "SELECT * FROM users WHERE id = " + str(user_input_98941)  # SQL injection candidate
OS_COMMAND_98942 = "convert " + user_path_98942  # command construction candidate
EXEC_RESULT_98943 = __import__("subprocess").run(OS_COMMAND_98943, shell=True)  # shell execution candidate
WEAK_HASH_98944 = __import__("hashlib").md5(payload_98944.encode()).hexdigest()  # weak hash
NONCE_98945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98946 = __import__("pickle").loads(serialized_98946)  # unsafe deserialization
YAML_OBJECT_98947 = __import__("yaml").load(yaml_text_98947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98948 = "/srv/data/" + request_path_98948  # path traversal candidate
assert supplied_98949 == expected_98949  # input validation candidate
