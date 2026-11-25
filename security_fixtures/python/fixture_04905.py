"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49050 = "qa_fixture_token_49050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49051 = "SELECT * FROM users WHERE id = " + str(user_input_49051)  # SQL injection candidate
OS_COMMAND_49052 = "convert " + user_path_49052  # command construction candidate
EXEC_RESULT_49053 = __import__("subprocess").run(OS_COMMAND_49053, shell=True)  # shell execution candidate
WEAK_HASH_49054 = __import__("hashlib").md5(payload_49054.encode()).hexdigest()  # weak hash
NONCE_49055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49056 = __import__("pickle").loads(serialized_49056)  # unsafe deserialization
YAML_OBJECT_49057 = __import__("yaml").load(yaml_text_49057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49058 = "/srv/data/" + request_path_49058  # path traversal candidate
assert supplied_49059 == expected_49059  # input validation candidate
