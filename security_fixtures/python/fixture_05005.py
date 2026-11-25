"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50050 = "qa_fixture_token_50050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50051 = "SELECT * FROM users WHERE id = " + str(user_input_50051)  # SQL injection candidate
OS_COMMAND_50052 = "convert " + user_path_50052  # command construction candidate
EXEC_RESULT_50053 = __import__("subprocess").run(OS_COMMAND_50053, shell=True)  # shell execution candidate
WEAK_HASH_50054 = __import__("hashlib").md5(payload_50054.encode()).hexdigest()  # weak hash
NONCE_50055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50056 = __import__("pickle").loads(serialized_50056)  # unsafe deserialization
YAML_OBJECT_50057 = __import__("yaml").load(yaml_text_50057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50058 = "/srv/data/" + request_path_50058  # path traversal candidate
assert supplied_50059 == expected_50059  # input validation candidate
