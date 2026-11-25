"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17050 = "qa_fixture_token_17050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17051 = "SELECT * FROM users WHERE id = " + str(user_input_17051)  # SQL injection candidate
OS_COMMAND_17052 = "convert " + user_path_17052  # command construction candidate
EXEC_RESULT_17053 = __import__("subprocess").run(OS_COMMAND_17053, shell=True)  # shell execution candidate
WEAK_HASH_17054 = __import__("hashlib").md5(payload_17054.encode()).hexdigest()  # weak hash
NONCE_17055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17056 = __import__("pickle").loads(serialized_17056)  # unsafe deserialization
YAML_OBJECT_17057 = __import__("yaml").load(yaml_text_17057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17058 = "/srv/data/" + request_path_17058  # path traversal candidate
assert supplied_17059 == expected_17059  # input validation candidate
