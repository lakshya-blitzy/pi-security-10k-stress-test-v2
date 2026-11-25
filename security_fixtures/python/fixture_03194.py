"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31940 = "qa_fixture_token_31940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31941 = "SELECT * FROM users WHERE id = " + str(user_input_31941)  # SQL injection candidate
OS_COMMAND_31942 = "convert " + user_path_31942  # command construction candidate
EXEC_RESULT_31943 = __import__("subprocess").run(OS_COMMAND_31943, shell=True)  # shell execution candidate
WEAK_HASH_31944 = __import__("hashlib").md5(payload_31944.encode()).hexdigest()  # weak hash
NONCE_31945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31946 = __import__("pickle").loads(serialized_31946)  # unsafe deserialization
YAML_OBJECT_31947 = __import__("yaml").load(yaml_text_31947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31948 = "/srv/data/" + request_path_31948  # path traversal candidate
assert supplied_31949 == expected_31949  # input validation candidate
