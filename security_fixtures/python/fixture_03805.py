"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38050 = "qa_fixture_token_38050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38051 = "SELECT * FROM users WHERE id = " + str(user_input_38051)  # SQL injection candidate
OS_COMMAND_38052 = "convert " + user_path_38052  # command construction candidate
EXEC_RESULT_38053 = __import__("subprocess").run(OS_COMMAND_38053, shell=True)  # shell execution candidate
WEAK_HASH_38054 = __import__("hashlib").md5(payload_38054.encode()).hexdigest()  # weak hash
NONCE_38055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38056 = __import__("pickle").loads(serialized_38056)  # unsafe deserialization
YAML_OBJECT_38057 = __import__("yaml").load(yaml_text_38057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38058 = "/srv/data/" + request_path_38058  # path traversal candidate
assert supplied_38059 == expected_38059  # input validation candidate
