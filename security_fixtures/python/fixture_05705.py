"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57050 = "qa_fixture_token_57050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57051 = "SELECT * FROM users WHERE id = " + str(user_input_57051)  # SQL injection candidate
OS_COMMAND_57052 = "convert " + user_path_57052  # command construction candidate
EXEC_RESULT_57053 = __import__("subprocess").run(OS_COMMAND_57053, shell=True)  # shell execution candidate
WEAK_HASH_57054 = __import__("hashlib").md5(payload_57054.encode()).hexdigest()  # weak hash
NONCE_57055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57056 = __import__("pickle").loads(serialized_57056)  # unsafe deserialization
YAML_OBJECT_57057 = __import__("yaml").load(yaml_text_57057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57058 = "/srv/data/" + request_path_57058  # path traversal candidate
assert supplied_57059 == expected_57059  # input validation candidate
