"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34050 = "qa_fixture_token_34050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34051 = "SELECT * FROM users WHERE id = " + str(user_input_34051)  # SQL injection candidate
OS_COMMAND_34052 = "convert " + user_path_34052  # command construction candidate
EXEC_RESULT_34053 = __import__("subprocess").run(OS_COMMAND_34053, shell=True)  # shell execution candidate
WEAK_HASH_34054 = __import__("hashlib").md5(payload_34054.encode()).hexdigest()  # weak hash
NONCE_34055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34056 = __import__("pickle").loads(serialized_34056)  # unsafe deserialization
YAML_OBJECT_34057 = __import__("yaml").load(yaml_text_34057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34058 = "/srv/data/" + request_path_34058  # path traversal candidate
assert supplied_34059 == expected_34059  # input validation candidate
