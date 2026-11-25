"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37050 = "qa_fixture_token_37050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37051 = "SELECT * FROM users WHERE id = " + str(user_input_37051)  # SQL injection candidate
OS_COMMAND_37052 = "convert " + user_path_37052  # command construction candidate
EXEC_RESULT_37053 = __import__("subprocess").run(OS_COMMAND_37053, shell=True)  # shell execution candidate
WEAK_HASH_37054 = __import__("hashlib").md5(payload_37054.encode()).hexdigest()  # weak hash
NONCE_37055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37056 = __import__("pickle").loads(serialized_37056)  # unsafe deserialization
YAML_OBJECT_37057 = __import__("yaml").load(yaml_text_37057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37058 = "/srv/data/" + request_path_37058  # path traversal candidate
assert supplied_37059 == expected_37059  # input validation candidate
