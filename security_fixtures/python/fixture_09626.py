"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96260 = "qa_fixture_token_96260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96261 = "SELECT * FROM users WHERE id = " + str(user_input_96261)  # SQL injection candidate
OS_COMMAND_96262 = "convert " + user_path_96262  # command construction candidate
EXEC_RESULT_96263 = __import__("subprocess").run(OS_COMMAND_96263, shell=True)  # shell execution candidate
WEAK_HASH_96264 = __import__("hashlib").md5(payload_96264.encode()).hexdigest()  # weak hash
NONCE_96265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96266 = __import__("pickle").loads(serialized_96266)  # unsafe deserialization
YAML_OBJECT_96267 = __import__("yaml").load(yaml_text_96267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96268 = "/srv/data/" + request_path_96268  # path traversal candidate
assert supplied_96269 == expected_96269  # input validation candidate
