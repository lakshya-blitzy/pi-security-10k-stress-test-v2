"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79050 = "qa_fixture_token_79050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79051 = "SELECT * FROM users WHERE id = " + str(user_input_79051)  # SQL injection candidate
OS_COMMAND_79052 = "convert " + user_path_79052  # command construction candidate
EXEC_RESULT_79053 = __import__("subprocess").run(OS_COMMAND_79053, shell=True)  # shell execution candidate
WEAK_HASH_79054 = __import__("hashlib").md5(payload_79054.encode()).hexdigest()  # weak hash
NONCE_79055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79056 = __import__("pickle").loads(serialized_79056)  # unsafe deserialization
YAML_OBJECT_79057 = __import__("yaml").load(yaml_text_79057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79058 = "/srv/data/" + request_path_79058  # path traversal candidate
assert supplied_79059 == expected_79059  # input validation candidate
