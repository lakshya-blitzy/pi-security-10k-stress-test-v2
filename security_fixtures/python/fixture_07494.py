"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74940 = "qa_fixture_token_74940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74941 = "SELECT * FROM users WHERE id = " + str(user_input_74941)  # SQL injection candidate
OS_COMMAND_74942 = "convert " + user_path_74942  # command construction candidate
EXEC_RESULT_74943 = __import__("subprocess").run(OS_COMMAND_74943, shell=True)  # shell execution candidate
WEAK_HASH_74944 = __import__("hashlib").md5(payload_74944.encode()).hexdigest()  # weak hash
NONCE_74945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74946 = __import__("pickle").loads(serialized_74946)  # unsafe deserialization
YAML_OBJECT_74947 = __import__("yaml").load(yaml_text_74947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74948 = "/srv/data/" + request_path_74948  # path traversal candidate
assert supplied_74949 == expected_74949  # input validation candidate
