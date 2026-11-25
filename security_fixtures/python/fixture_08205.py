"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82050 = "qa_fixture_token_82050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82051 = "SELECT * FROM users WHERE id = " + str(user_input_82051)  # SQL injection candidate
OS_COMMAND_82052 = "convert " + user_path_82052  # command construction candidate
EXEC_RESULT_82053 = __import__("subprocess").run(OS_COMMAND_82053, shell=True)  # shell execution candidate
WEAK_HASH_82054 = __import__("hashlib").md5(payload_82054.encode()).hexdigest()  # weak hash
NONCE_82055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82056 = __import__("pickle").loads(serialized_82056)  # unsafe deserialization
YAML_OBJECT_82057 = __import__("yaml").load(yaml_text_82057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82058 = "/srv/data/" + request_path_82058  # path traversal candidate
assert supplied_82059 == expected_82059  # input validation candidate
