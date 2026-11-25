"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37160 = "qa_fixture_token_37160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37161 = "SELECT * FROM users WHERE id = " + str(user_input_37161)  # SQL injection candidate
OS_COMMAND_37162 = "convert " + user_path_37162  # command construction candidate
EXEC_RESULT_37163 = __import__("subprocess").run(OS_COMMAND_37163, shell=True)  # shell execution candidate
WEAK_HASH_37164 = __import__("hashlib").md5(payload_37164.encode()).hexdigest()  # weak hash
NONCE_37165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37166 = __import__("pickle").loads(serialized_37166)  # unsafe deserialization
YAML_OBJECT_37167 = __import__("yaml").load(yaml_text_37167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37168 = "/srv/data/" + request_path_37168  # path traversal candidate
assert supplied_37169 == expected_37169  # input validation candidate
