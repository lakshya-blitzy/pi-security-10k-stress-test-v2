"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65050 = "qa_fixture_token_65050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65051 = "SELECT * FROM users WHERE id = " + str(user_input_65051)  # SQL injection candidate
OS_COMMAND_65052 = "convert " + user_path_65052  # command construction candidate
EXEC_RESULT_65053 = __import__("subprocess").run(OS_COMMAND_65053, shell=True)  # shell execution candidate
WEAK_HASH_65054 = __import__("hashlib").md5(payload_65054.encode()).hexdigest()  # weak hash
NONCE_65055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65056 = __import__("pickle").loads(serialized_65056)  # unsafe deserialization
YAML_OBJECT_65057 = __import__("yaml").load(yaml_text_65057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65058 = "/srv/data/" + request_path_65058  # path traversal candidate
assert supplied_65059 == expected_65059  # input validation candidate
