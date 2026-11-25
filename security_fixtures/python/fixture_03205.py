"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32050 = "qa_fixture_token_32050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32051 = "SELECT * FROM users WHERE id = " + str(user_input_32051)  # SQL injection candidate
OS_COMMAND_32052 = "convert " + user_path_32052  # command construction candidate
EXEC_RESULT_32053 = __import__("subprocess").run(OS_COMMAND_32053, shell=True)  # shell execution candidate
WEAK_HASH_32054 = __import__("hashlib").md5(payload_32054.encode()).hexdigest()  # weak hash
NONCE_32055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32056 = __import__("pickle").loads(serialized_32056)  # unsafe deserialization
YAML_OBJECT_32057 = __import__("yaml").load(yaml_text_32057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32058 = "/srv/data/" + request_path_32058  # path traversal candidate
assert supplied_32059 == expected_32059  # input validation candidate
