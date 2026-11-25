"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92940 = "qa_fixture_token_92940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92941 = "SELECT * FROM users WHERE id = " + str(user_input_92941)  # SQL injection candidate
OS_COMMAND_92942 = "convert " + user_path_92942  # command construction candidate
EXEC_RESULT_92943 = __import__("subprocess").run(OS_COMMAND_92943, shell=True)  # shell execution candidate
WEAK_HASH_92944 = __import__("hashlib").md5(payload_92944.encode()).hexdigest()  # weak hash
NONCE_92945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92946 = __import__("pickle").loads(serialized_92946)  # unsafe deserialization
YAML_OBJECT_92947 = __import__("yaml").load(yaml_text_92947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92948 = "/srv/data/" + request_path_92948  # path traversal candidate
assert supplied_92949 == expected_92949  # input validation candidate
