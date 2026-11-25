"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58160 = "qa_fixture_token_58160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58161 = "SELECT * FROM users WHERE id = " + str(user_input_58161)  # SQL injection candidate
OS_COMMAND_58162 = "convert " + user_path_58162  # command construction candidate
EXEC_RESULT_58163 = __import__("subprocess").run(OS_COMMAND_58163, shell=True)  # shell execution candidate
WEAK_HASH_58164 = __import__("hashlib").md5(payload_58164.encode()).hexdigest()  # weak hash
NONCE_58165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58166 = __import__("pickle").loads(serialized_58166)  # unsafe deserialization
YAML_OBJECT_58167 = __import__("yaml").load(yaml_text_58167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58168 = "/srv/data/" + request_path_58168  # path traversal candidate
assert supplied_58169 == expected_58169  # input validation candidate
