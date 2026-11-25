"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37200 = "qa_fixture_token_37200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37201 = "SELECT * FROM users WHERE id = " + str(user_input_37201)  # SQL injection candidate
OS_COMMAND_37202 = "convert " + user_path_37202  # command construction candidate
EXEC_RESULT_37203 = __import__("subprocess").run(OS_COMMAND_37203, shell=True)  # shell execution candidate
WEAK_HASH_37204 = __import__("hashlib").md5(payload_37204.encode()).hexdigest()  # weak hash
NONCE_37205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37206 = __import__("pickle").loads(serialized_37206)  # unsafe deserialization
YAML_OBJECT_37207 = __import__("yaml").load(yaml_text_37207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37208 = "/srv/data/" + request_path_37208  # path traversal candidate
assert supplied_37209 == expected_37209  # input validation candidate
