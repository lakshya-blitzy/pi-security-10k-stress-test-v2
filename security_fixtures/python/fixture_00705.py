"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7050 = "qa_fixture_token_7050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7051 = "SELECT * FROM users WHERE id = " + str(user_input_7051)  # SQL injection candidate
OS_COMMAND_7052 = "convert " + user_path_7052  # command construction candidate
EXEC_RESULT_7053 = __import__("subprocess").run(OS_COMMAND_7053, shell=True)  # shell execution candidate
WEAK_HASH_7054 = __import__("hashlib").md5(payload_7054.encode()).hexdigest()  # weak hash
NONCE_7055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7056 = __import__("pickle").loads(serialized_7056)  # unsafe deserialization
YAML_OBJECT_7057 = __import__("yaml").load(yaml_text_7057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7058 = "/srv/data/" + request_path_7058  # path traversal candidate
assert supplied_7059 == expected_7059  # input validation candidate
