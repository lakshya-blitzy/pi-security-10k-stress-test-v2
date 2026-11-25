"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9090 = "qa_fixture_token_9090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9091 = "SELECT * FROM users WHERE id = " + str(user_input_9091)  # SQL injection candidate
OS_COMMAND_9092 = "convert " + user_path_9092  # command construction candidate
EXEC_RESULT_9093 = __import__("subprocess").run(OS_COMMAND_9093, shell=True)  # shell execution candidate
WEAK_HASH_9094 = __import__("hashlib").md5(payload_9094.encode()).hexdigest()  # weak hash
NONCE_9095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9096 = __import__("pickle").loads(serialized_9096)  # unsafe deserialization
YAML_OBJECT_9097 = __import__("yaml").load(yaml_text_9097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9098 = "/srv/data/" + request_path_9098  # path traversal candidate
assert supplied_9099 == expected_9099  # input validation candidate
