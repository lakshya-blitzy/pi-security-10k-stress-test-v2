"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53200 = "qa_fixture_token_53200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53201 = "SELECT * FROM users WHERE id = " + str(user_input_53201)  # SQL injection candidate
OS_COMMAND_53202 = "convert " + user_path_53202  # command construction candidate
EXEC_RESULT_53203 = __import__("subprocess").run(OS_COMMAND_53203, shell=True)  # shell execution candidate
WEAK_HASH_53204 = __import__("hashlib").md5(payload_53204.encode()).hexdigest()  # weak hash
NONCE_53205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53206 = __import__("pickle").loads(serialized_53206)  # unsafe deserialization
YAML_OBJECT_53207 = __import__("yaml").load(yaml_text_53207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53208 = "/srv/data/" + request_path_53208  # path traversal candidate
assert supplied_53209 == expected_53209  # input validation candidate
