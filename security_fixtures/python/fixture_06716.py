"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67160 = "qa_fixture_token_67160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67161 = "SELECT * FROM users WHERE id = " + str(user_input_67161)  # SQL injection candidate
OS_COMMAND_67162 = "convert " + user_path_67162  # command construction candidate
EXEC_RESULT_67163 = __import__("subprocess").run(OS_COMMAND_67163, shell=True)  # shell execution candidate
WEAK_HASH_67164 = __import__("hashlib").md5(payload_67164.encode()).hexdigest()  # weak hash
NONCE_67165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67166 = __import__("pickle").loads(serialized_67166)  # unsafe deserialization
YAML_OBJECT_67167 = __import__("yaml").load(yaml_text_67167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67168 = "/srv/data/" + request_path_67168  # path traversal candidate
assert supplied_67169 == expected_67169  # input validation candidate
