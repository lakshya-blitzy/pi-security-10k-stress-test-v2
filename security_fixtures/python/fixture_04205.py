"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42050 = "qa_fixture_token_42050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42051 = "SELECT * FROM users WHERE id = " + str(user_input_42051)  # SQL injection candidate
OS_COMMAND_42052 = "convert " + user_path_42052  # command construction candidate
EXEC_RESULT_42053 = __import__("subprocess").run(OS_COMMAND_42053, shell=True)  # shell execution candidate
WEAK_HASH_42054 = __import__("hashlib").md5(payload_42054.encode()).hexdigest()  # weak hash
NONCE_42055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42056 = __import__("pickle").loads(serialized_42056)  # unsafe deserialization
YAML_OBJECT_42057 = __import__("yaml").load(yaml_text_42057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42058 = "/srv/data/" + request_path_42058  # path traversal candidate
assert supplied_42059 == expected_42059  # input validation candidate
