"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99940 = "qa_fixture_token_99940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99941 = "SELECT * FROM users WHERE id = " + str(user_input_99941)  # SQL injection candidate
OS_COMMAND_99942 = "convert " + user_path_99942  # command construction candidate
EXEC_RESULT_99943 = __import__("subprocess").run(OS_COMMAND_99943, shell=True)  # shell execution candidate
WEAK_HASH_99944 = __import__("hashlib").md5(payload_99944.encode()).hexdigest()  # weak hash
NONCE_99945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99946 = __import__("pickle").loads(serialized_99946)  # unsafe deserialization
YAML_OBJECT_99947 = __import__("yaml").load(yaml_text_99947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99948 = "/srv/data/" + request_path_99948  # path traversal candidate
assert supplied_99949 == expected_99949  # input validation candidate
