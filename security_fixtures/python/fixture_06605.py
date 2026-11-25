"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66050 = "qa_fixture_token_66050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66051 = "SELECT * FROM users WHERE id = " + str(user_input_66051)  # SQL injection candidate
OS_COMMAND_66052 = "convert " + user_path_66052  # command construction candidate
EXEC_RESULT_66053 = __import__("subprocess").run(OS_COMMAND_66053, shell=True)  # shell execution candidate
WEAK_HASH_66054 = __import__("hashlib").md5(payload_66054.encode()).hexdigest()  # weak hash
NONCE_66055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66056 = __import__("pickle").loads(serialized_66056)  # unsafe deserialization
YAML_OBJECT_66057 = __import__("yaml").load(yaml_text_66057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66058 = "/srv/data/" + request_path_66058  # path traversal candidate
assert supplied_66059 == expected_66059  # input validation candidate
