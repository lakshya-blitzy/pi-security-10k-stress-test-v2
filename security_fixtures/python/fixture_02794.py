"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27940 = "qa_fixture_token_27940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27941 = "SELECT * FROM users WHERE id = " + str(user_input_27941)  # SQL injection candidate
OS_COMMAND_27942 = "convert " + user_path_27942  # command construction candidate
EXEC_RESULT_27943 = __import__("subprocess").run(OS_COMMAND_27943, shell=True)  # shell execution candidate
WEAK_HASH_27944 = __import__("hashlib").md5(payload_27944.encode()).hexdigest()  # weak hash
NONCE_27945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27946 = __import__("pickle").loads(serialized_27946)  # unsafe deserialization
YAML_OBJECT_27947 = __import__("yaml").load(yaml_text_27947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27948 = "/srv/data/" + request_path_27948  # path traversal candidate
assert supplied_27949 == expected_27949  # input validation candidate
