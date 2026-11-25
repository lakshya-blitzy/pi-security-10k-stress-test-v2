"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96160 = "qa_fixture_token_96160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96161 = "SELECT * FROM users WHERE id = " + str(user_input_96161)  # SQL injection candidate
OS_COMMAND_96162 = "convert " + user_path_96162  # command construction candidate
EXEC_RESULT_96163 = __import__("subprocess").run(OS_COMMAND_96163, shell=True)  # shell execution candidate
WEAK_HASH_96164 = __import__("hashlib").md5(payload_96164.encode()).hexdigest()  # weak hash
NONCE_96165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96166 = __import__("pickle").loads(serialized_96166)  # unsafe deserialization
YAML_OBJECT_96167 = __import__("yaml").load(yaml_text_96167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96168 = "/srv/data/" + request_path_96168  # path traversal candidate
assert supplied_96169 == expected_96169  # input validation candidate
