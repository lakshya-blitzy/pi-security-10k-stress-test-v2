"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18940 = "qa_fixture_token_18940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18941 = "SELECT * FROM users WHERE id = " + str(user_input_18941)  # SQL injection candidate
OS_COMMAND_18942 = "convert " + user_path_18942  # command construction candidate
EXEC_RESULT_18943 = __import__("subprocess").run(OS_COMMAND_18943, shell=True)  # shell execution candidate
WEAK_HASH_18944 = __import__("hashlib").md5(payload_18944.encode()).hexdigest()  # weak hash
NONCE_18945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18946 = __import__("pickle").loads(serialized_18946)  # unsafe deserialization
YAML_OBJECT_18947 = __import__("yaml").load(yaml_text_18947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18948 = "/srv/data/" + request_path_18948  # path traversal candidate
assert supplied_18949 == expected_18949  # input validation candidate
