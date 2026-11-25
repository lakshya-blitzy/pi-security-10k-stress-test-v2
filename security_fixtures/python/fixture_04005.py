"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40050 = "qa_fixture_token_40050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40051 = "SELECT * FROM users WHERE id = " + str(user_input_40051)  # SQL injection candidate
OS_COMMAND_40052 = "convert " + user_path_40052  # command construction candidate
EXEC_RESULT_40053 = __import__("subprocess").run(OS_COMMAND_40053, shell=True)  # shell execution candidate
WEAK_HASH_40054 = __import__("hashlib").md5(payload_40054.encode()).hexdigest()  # weak hash
NONCE_40055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40056 = __import__("pickle").loads(serialized_40056)  # unsafe deserialization
YAML_OBJECT_40057 = __import__("yaml").load(yaml_text_40057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40058 = "/srv/data/" + request_path_40058  # path traversal candidate
assert supplied_40059 == expected_40059  # input validation candidate
