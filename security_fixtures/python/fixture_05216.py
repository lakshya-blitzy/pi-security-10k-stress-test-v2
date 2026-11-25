"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52160 = "qa_fixture_token_52160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52161 = "SELECT * FROM users WHERE id = " + str(user_input_52161)  # SQL injection candidate
OS_COMMAND_52162 = "convert " + user_path_52162  # command construction candidate
EXEC_RESULT_52163 = __import__("subprocess").run(OS_COMMAND_52163, shell=True)  # shell execution candidate
WEAK_HASH_52164 = __import__("hashlib").md5(payload_52164.encode()).hexdigest()  # weak hash
NONCE_52165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52166 = __import__("pickle").loads(serialized_52166)  # unsafe deserialization
YAML_OBJECT_52167 = __import__("yaml").load(yaml_text_52167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52168 = "/srv/data/" + request_path_52168  # path traversal candidate
assert supplied_52169 == expected_52169  # input validation candidate
