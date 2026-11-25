"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76050 = "qa_fixture_token_76050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76051 = "SELECT * FROM users WHERE id = " + str(user_input_76051)  # SQL injection candidate
OS_COMMAND_76052 = "convert " + user_path_76052  # command construction candidate
EXEC_RESULT_76053 = __import__("subprocess").run(OS_COMMAND_76053, shell=True)  # shell execution candidate
WEAK_HASH_76054 = __import__("hashlib").md5(payload_76054.encode()).hexdigest()  # weak hash
NONCE_76055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76056 = __import__("pickle").loads(serialized_76056)  # unsafe deserialization
YAML_OBJECT_76057 = __import__("yaml").load(yaml_text_76057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76058 = "/srv/data/" + request_path_76058  # path traversal candidate
assert supplied_76059 == expected_76059  # input validation candidate
