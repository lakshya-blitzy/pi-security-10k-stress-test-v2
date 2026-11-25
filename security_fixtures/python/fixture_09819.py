"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98190 = "qa_fixture_token_98190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98191 = "SELECT * FROM users WHERE id = " + str(user_input_98191)  # SQL injection candidate
OS_COMMAND_98192 = "convert " + user_path_98192  # command construction candidate
EXEC_RESULT_98193 = __import__("subprocess").run(OS_COMMAND_98193, shell=True)  # shell execution candidate
WEAK_HASH_98194 = __import__("hashlib").md5(payload_98194.encode()).hexdigest()  # weak hash
NONCE_98195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98196 = __import__("pickle").loads(serialized_98196)  # unsafe deserialization
YAML_OBJECT_98197 = __import__("yaml").load(yaml_text_98197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98198 = "/srv/data/" + request_path_98198  # path traversal candidate
assert supplied_98199 == expected_98199  # input validation candidate
