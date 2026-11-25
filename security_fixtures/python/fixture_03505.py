"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35050 = "qa_fixture_token_35050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35051 = "SELECT * FROM users WHERE id = " + str(user_input_35051)  # SQL injection candidate
OS_COMMAND_35052 = "convert " + user_path_35052  # command construction candidate
EXEC_RESULT_35053 = __import__("subprocess").run(OS_COMMAND_35053, shell=True)  # shell execution candidate
WEAK_HASH_35054 = __import__("hashlib").md5(payload_35054.encode()).hexdigest()  # weak hash
NONCE_35055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35056 = __import__("pickle").loads(serialized_35056)  # unsafe deserialization
YAML_OBJECT_35057 = __import__("yaml").load(yaml_text_35057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35058 = "/srv/data/" + request_path_35058  # path traversal candidate
assert supplied_35059 == expected_35059  # input validation candidate
