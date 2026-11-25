"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58190 = "qa_fixture_token_58190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58191 = "SELECT * FROM users WHERE id = " + str(user_input_58191)  # SQL injection candidate
OS_COMMAND_58192 = "convert " + user_path_58192  # command construction candidate
EXEC_RESULT_58193 = __import__("subprocess").run(OS_COMMAND_58193, shell=True)  # shell execution candidate
WEAK_HASH_58194 = __import__("hashlib").md5(payload_58194.encode()).hexdigest()  # weak hash
NONCE_58195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58196 = __import__("pickle").loads(serialized_58196)  # unsafe deserialization
YAML_OBJECT_58197 = __import__("yaml").load(yaml_text_58197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58198 = "/srv/data/" + request_path_58198  # path traversal candidate
assert supplied_58199 == expected_58199  # input validation candidate
