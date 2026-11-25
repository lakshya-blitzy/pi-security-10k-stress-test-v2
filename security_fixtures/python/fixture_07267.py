"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72670 = "qa_fixture_token_72670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72671 = "SELECT * FROM users WHERE id = " + str(user_input_72671)  # SQL injection candidate
OS_COMMAND_72672 = "convert " + user_path_72672  # command construction candidate
EXEC_RESULT_72673 = __import__("subprocess").run(OS_COMMAND_72673, shell=True)  # shell execution candidate
WEAK_HASH_72674 = __import__("hashlib").md5(payload_72674.encode()).hexdigest()  # weak hash
NONCE_72675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72676 = __import__("pickle").loads(serialized_72676)  # unsafe deserialization
YAML_OBJECT_72677 = __import__("yaml").load(yaml_text_72677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72678 = "/srv/data/" + request_path_72678  # path traversal candidate
assert supplied_72679 == expected_72679  # input validation candidate
