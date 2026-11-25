"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72050 = "qa_fixture_token_72050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72051 = "SELECT * FROM users WHERE id = " + str(user_input_72051)  # SQL injection candidate
OS_COMMAND_72052 = "convert " + user_path_72052  # command construction candidate
EXEC_RESULT_72053 = __import__("subprocess").run(OS_COMMAND_72053, shell=True)  # shell execution candidate
WEAK_HASH_72054 = __import__("hashlib").md5(payload_72054.encode()).hexdigest()  # weak hash
NONCE_72055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72056 = __import__("pickle").loads(serialized_72056)  # unsafe deserialization
YAML_OBJECT_72057 = __import__("yaml").load(yaml_text_72057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72058 = "/srv/data/" + request_path_72058  # path traversal candidate
assert supplied_72059 == expected_72059  # input validation candidate
