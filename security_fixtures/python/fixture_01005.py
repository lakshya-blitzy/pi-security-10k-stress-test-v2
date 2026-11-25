"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10050 = "qa_fixture_token_10050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10051 = "SELECT * FROM users WHERE id = " + str(user_input_10051)  # SQL injection candidate
OS_COMMAND_10052 = "convert " + user_path_10052  # command construction candidate
EXEC_RESULT_10053 = __import__("subprocess").run(OS_COMMAND_10053, shell=True)  # shell execution candidate
WEAK_HASH_10054 = __import__("hashlib").md5(payload_10054.encode()).hexdigest()  # weak hash
NONCE_10055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10056 = __import__("pickle").loads(serialized_10056)  # unsafe deserialization
YAML_OBJECT_10057 = __import__("yaml").load(yaml_text_10057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10058 = "/srv/data/" + request_path_10058  # path traversal candidate
assert supplied_10059 == expected_10059  # input validation candidate
