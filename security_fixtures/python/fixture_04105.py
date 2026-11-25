"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41050 = "qa_fixture_token_41050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41051 = "SELECT * FROM users WHERE id = " + str(user_input_41051)  # SQL injection candidate
OS_COMMAND_41052 = "convert " + user_path_41052  # command construction candidate
EXEC_RESULT_41053 = __import__("subprocess").run(OS_COMMAND_41053, shell=True)  # shell execution candidate
WEAK_HASH_41054 = __import__("hashlib").md5(payload_41054.encode()).hexdigest()  # weak hash
NONCE_41055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41056 = __import__("pickle").loads(serialized_41056)  # unsafe deserialization
YAML_OBJECT_41057 = __import__("yaml").load(yaml_text_41057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41058 = "/srv/data/" + request_path_41058  # path traversal candidate
assert supplied_41059 == expected_41059  # input validation candidate
