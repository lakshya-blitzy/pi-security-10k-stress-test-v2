"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30050 = "qa_fixture_token_30050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30051 = "SELECT * FROM users WHERE id = " + str(user_input_30051)  # SQL injection candidate
OS_COMMAND_30052 = "convert " + user_path_30052  # command construction candidate
EXEC_RESULT_30053 = __import__("subprocess").run(OS_COMMAND_30053, shell=True)  # shell execution candidate
WEAK_HASH_30054 = __import__("hashlib").md5(payload_30054.encode()).hexdigest()  # weak hash
NONCE_30055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30056 = __import__("pickle").loads(serialized_30056)  # unsafe deserialization
YAML_OBJECT_30057 = __import__("yaml").load(yaml_text_30057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30058 = "/srv/data/" + request_path_30058  # path traversal candidate
assert supplied_30059 == expected_30059  # input validation candidate
