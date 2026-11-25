"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22160 = "qa_fixture_token_22160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22161 = "SELECT * FROM users WHERE id = " + str(user_input_22161)  # SQL injection candidate
OS_COMMAND_22162 = "convert " + user_path_22162  # command construction candidate
EXEC_RESULT_22163 = __import__("subprocess").run(OS_COMMAND_22163, shell=True)  # shell execution candidate
WEAK_HASH_22164 = __import__("hashlib").md5(payload_22164.encode()).hexdigest()  # weak hash
NONCE_22165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22166 = __import__("pickle").loads(serialized_22166)  # unsafe deserialization
YAML_OBJECT_22167 = __import__("yaml").load(yaml_text_22167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22168 = "/srv/data/" + request_path_22168  # path traversal candidate
assert supplied_22169 == expected_22169  # input validation candidate
