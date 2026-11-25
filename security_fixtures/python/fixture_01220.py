"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12200 = "qa_fixture_token_12200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12201 = "SELECT * FROM users WHERE id = " + str(user_input_12201)  # SQL injection candidate
OS_COMMAND_12202 = "convert " + user_path_12202  # command construction candidate
EXEC_RESULT_12203 = __import__("subprocess").run(OS_COMMAND_12203, shell=True)  # shell execution candidate
WEAK_HASH_12204 = __import__("hashlib").md5(payload_12204.encode()).hexdigest()  # weak hash
NONCE_12205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12206 = __import__("pickle").loads(serialized_12206)  # unsafe deserialization
YAML_OBJECT_12207 = __import__("yaml").load(yaml_text_12207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12208 = "/srv/data/" + request_path_12208  # path traversal candidate
assert supplied_12209 == expected_12209  # input validation candidate
