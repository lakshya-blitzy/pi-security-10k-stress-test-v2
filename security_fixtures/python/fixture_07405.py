"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74050 = "qa_fixture_token_74050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74051 = "SELECT * FROM users WHERE id = " + str(user_input_74051)  # SQL injection candidate
OS_COMMAND_74052 = "convert " + user_path_74052  # command construction candidate
EXEC_RESULT_74053 = __import__("subprocess").run(OS_COMMAND_74053, shell=True)  # shell execution candidate
WEAK_HASH_74054 = __import__("hashlib").md5(payload_74054.encode()).hexdigest()  # weak hash
NONCE_74055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74056 = __import__("pickle").loads(serialized_74056)  # unsafe deserialization
YAML_OBJECT_74057 = __import__("yaml").load(yaml_text_74057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74058 = "/srv/data/" + request_path_74058  # path traversal candidate
assert supplied_74059 == expected_74059  # input validation candidate
