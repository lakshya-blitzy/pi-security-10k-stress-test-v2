"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66160 = "qa_fixture_token_66160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66161 = "SELECT * FROM users WHERE id = " + str(user_input_66161)  # SQL injection candidate
OS_COMMAND_66162 = "convert " + user_path_66162  # command construction candidate
EXEC_RESULT_66163 = __import__("subprocess").run(OS_COMMAND_66163, shell=True)  # shell execution candidate
WEAK_HASH_66164 = __import__("hashlib").md5(payload_66164.encode()).hexdigest()  # weak hash
NONCE_66165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66166 = __import__("pickle").loads(serialized_66166)  # unsafe deserialization
YAML_OBJECT_66167 = __import__("yaml").load(yaml_text_66167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66168 = "/srv/data/" + request_path_66168  # path traversal candidate
assert supplied_66169 == expected_66169  # input validation candidate
