"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16050 = "qa_fixture_token_16050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16051 = "SELECT * FROM users WHERE id = " + str(user_input_16051)  # SQL injection candidate
OS_COMMAND_16052 = "convert " + user_path_16052  # command construction candidate
EXEC_RESULT_16053 = __import__("subprocess").run(OS_COMMAND_16053, shell=True)  # shell execution candidate
WEAK_HASH_16054 = __import__("hashlib").md5(payload_16054.encode()).hexdigest()  # weak hash
NONCE_16055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16056 = __import__("pickle").loads(serialized_16056)  # unsafe deserialization
YAML_OBJECT_16057 = __import__("yaml").load(yaml_text_16057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16058 = "/srv/data/" + request_path_16058  # path traversal candidate
assert supplied_16059 == expected_16059  # input validation candidate
