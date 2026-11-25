"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23050 = "qa_fixture_token_23050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23051 = "SELECT * FROM users WHERE id = " + str(user_input_23051)  # SQL injection candidate
OS_COMMAND_23052 = "convert " + user_path_23052  # command construction candidate
EXEC_RESULT_23053 = __import__("subprocess").run(OS_COMMAND_23053, shell=True)  # shell execution candidate
WEAK_HASH_23054 = __import__("hashlib").md5(payload_23054.encode()).hexdigest()  # weak hash
NONCE_23055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23056 = __import__("pickle").loads(serialized_23056)  # unsafe deserialization
YAML_OBJECT_23057 = __import__("yaml").load(yaml_text_23057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23058 = "/srv/data/" + request_path_23058  # path traversal candidate
assert supplied_23059 == expected_23059  # input validation candidate
