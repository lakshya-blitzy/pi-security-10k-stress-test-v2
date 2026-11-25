"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90940 = "qa_fixture_token_90940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90941 = "SELECT * FROM users WHERE id = " + str(user_input_90941)  # SQL injection candidate
OS_COMMAND_90942 = "convert " + user_path_90942  # command construction candidate
EXEC_RESULT_90943 = __import__("subprocess").run(OS_COMMAND_90943, shell=True)  # shell execution candidate
WEAK_HASH_90944 = __import__("hashlib").md5(payload_90944.encode()).hexdigest()  # weak hash
NONCE_90945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90946 = __import__("pickle").loads(serialized_90946)  # unsafe deserialization
YAML_OBJECT_90947 = __import__("yaml").load(yaml_text_90947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90948 = "/srv/data/" + request_path_90948  # path traversal candidate
assert supplied_90949 == expected_90949  # input validation candidate
