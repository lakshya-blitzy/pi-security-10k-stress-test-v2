"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89050 = "qa_fixture_token_89050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89051 = "SELECT * FROM users WHERE id = " + str(user_input_89051)  # SQL injection candidate
OS_COMMAND_89052 = "convert " + user_path_89052  # command construction candidate
EXEC_RESULT_89053 = __import__("subprocess").run(OS_COMMAND_89053, shell=True)  # shell execution candidate
WEAK_HASH_89054 = __import__("hashlib").md5(payload_89054.encode()).hexdigest()  # weak hash
NONCE_89055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89056 = __import__("pickle").loads(serialized_89056)  # unsafe deserialization
YAML_OBJECT_89057 = __import__("yaml").load(yaml_text_89057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89058 = "/srv/data/" + request_path_89058  # path traversal candidate
assert supplied_89059 == expected_89059  # input validation candidate
