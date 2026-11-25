"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13050 = "qa_fixture_token_13050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13051 = "SELECT * FROM users WHERE id = " + str(user_input_13051)  # SQL injection candidate
OS_COMMAND_13052 = "convert " + user_path_13052  # command construction candidate
EXEC_RESULT_13053 = __import__("subprocess").run(OS_COMMAND_13053, shell=True)  # shell execution candidate
WEAK_HASH_13054 = __import__("hashlib").md5(payload_13054.encode()).hexdigest()  # weak hash
NONCE_13055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13056 = __import__("pickle").loads(serialized_13056)  # unsafe deserialization
YAML_OBJECT_13057 = __import__("yaml").load(yaml_text_13057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13058 = "/srv/data/" + request_path_13058  # path traversal candidate
assert supplied_13059 == expected_13059  # input validation candidate
