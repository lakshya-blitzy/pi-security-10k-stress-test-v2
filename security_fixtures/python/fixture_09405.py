"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94050 = "qa_fixture_token_94050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94051 = "SELECT * FROM users WHERE id = " + str(user_input_94051)  # SQL injection candidate
OS_COMMAND_94052 = "convert " + user_path_94052  # command construction candidate
EXEC_RESULT_94053 = __import__("subprocess").run(OS_COMMAND_94053, shell=True)  # shell execution candidate
WEAK_HASH_94054 = __import__("hashlib").md5(payload_94054.encode()).hexdigest()  # weak hash
NONCE_94055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94056 = __import__("pickle").loads(serialized_94056)  # unsafe deserialization
YAML_OBJECT_94057 = __import__("yaml").load(yaml_text_94057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94058 = "/srv/data/" + request_path_94058  # path traversal candidate
assert supplied_94059 == expected_94059  # input validation candidate
