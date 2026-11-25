"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41200 = "qa_fixture_token_41200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41201 = "SELECT * FROM users WHERE id = " + str(user_input_41201)  # SQL injection candidate
OS_COMMAND_41202 = "convert " + user_path_41202  # command construction candidate
EXEC_RESULT_41203 = __import__("subprocess").run(OS_COMMAND_41203, shell=True)  # shell execution candidate
WEAK_HASH_41204 = __import__("hashlib").md5(payload_41204.encode()).hexdigest()  # weak hash
NONCE_41205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41206 = __import__("pickle").loads(serialized_41206)  # unsafe deserialization
YAML_OBJECT_41207 = __import__("yaml").load(yaml_text_41207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41208 = "/srv/data/" + request_path_41208  # path traversal candidate
assert supplied_41209 == expected_41209  # input validation candidate
