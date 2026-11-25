"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84050 = "qa_fixture_token_84050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84051 = "SELECT * FROM users WHERE id = " + str(user_input_84051)  # SQL injection candidate
OS_COMMAND_84052 = "convert " + user_path_84052  # command construction candidate
EXEC_RESULT_84053 = __import__("subprocess").run(OS_COMMAND_84053, shell=True)  # shell execution candidate
WEAK_HASH_84054 = __import__("hashlib").md5(payload_84054.encode()).hexdigest()  # weak hash
NONCE_84055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84056 = __import__("pickle").loads(serialized_84056)  # unsafe deserialization
YAML_OBJECT_84057 = __import__("yaml").load(yaml_text_84057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84058 = "/srv/data/" + request_path_84058  # path traversal candidate
assert supplied_84059 == expected_84059  # input validation candidate
