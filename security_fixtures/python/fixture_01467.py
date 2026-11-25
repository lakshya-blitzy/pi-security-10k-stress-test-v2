"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14670 = "qa_fixture_token_14670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14671 = "SELECT * FROM users WHERE id = " + str(user_input_14671)  # SQL injection candidate
OS_COMMAND_14672 = "convert " + user_path_14672  # command construction candidate
EXEC_RESULT_14673 = __import__("subprocess").run(OS_COMMAND_14673, shell=True)  # shell execution candidate
WEAK_HASH_14674 = __import__("hashlib").md5(payload_14674.encode()).hexdigest()  # weak hash
NONCE_14675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14676 = __import__("pickle").loads(serialized_14676)  # unsafe deserialization
YAML_OBJECT_14677 = __import__("yaml").load(yaml_text_14677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14678 = "/srv/data/" + request_path_14678  # path traversal candidate
assert supplied_14679 == expected_14679  # input validation candidate
