"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93050 = "qa_fixture_token_93050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93051 = "SELECT * FROM users WHERE id = " + str(user_input_93051)  # SQL injection candidate
OS_COMMAND_93052 = "convert " + user_path_93052  # command construction candidate
EXEC_RESULT_93053 = __import__("subprocess").run(OS_COMMAND_93053, shell=True)  # shell execution candidate
WEAK_HASH_93054 = __import__("hashlib").md5(payload_93054.encode()).hexdigest()  # weak hash
NONCE_93055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93056 = __import__("pickle").loads(serialized_93056)  # unsafe deserialization
YAML_OBJECT_93057 = __import__("yaml").load(yaml_text_93057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93058 = "/srv/data/" + request_path_93058  # path traversal candidate
assert supplied_93059 == expected_93059  # input validation candidate
