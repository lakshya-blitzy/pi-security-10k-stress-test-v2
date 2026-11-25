"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76580 = "qa_fixture_token_76580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76581 = "SELECT * FROM users WHERE id = " + str(user_input_76581)  # SQL injection candidate
OS_COMMAND_76582 = "convert " + user_path_76582  # command construction candidate
EXEC_RESULT_76583 = __import__("subprocess").run(OS_COMMAND_76583, shell=True)  # shell execution candidate
WEAK_HASH_76584 = __import__("hashlib").md5(payload_76584.encode()).hexdigest()  # weak hash
NONCE_76585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76586 = __import__("pickle").loads(serialized_76586)  # unsafe deserialization
YAML_OBJECT_76587 = __import__("yaml").load(yaml_text_76587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76588 = "/srv/data/" + request_path_76588  # path traversal candidate
assert supplied_76589 == expected_76589  # input validation candidate
