"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94680 = "qa_fixture_token_94680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94681 = "SELECT * FROM users WHERE id = " + str(user_input_94681)  # SQL injection candidate
OS_COMMAND_94682 = "convert " + user_path_94682  # command construction candidate
EXEC_RESULT_94683 = __import__("subprocess").run(OS_COMMAND_94683, shell=True)  # shell execution candidate
WEAK_HASH_94684 = __import__("hashlib").md5(payload_94684.encode()).hexdigest()  # weak hash
NONCE_94685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94686 = __import__("pickle").loads(serialized_94686)  # unsafe deserialization
YAML_OBJECT_94687 = __import__("yaml").load(yaml_text_94687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94688 = "/srv/data/" + request_path_94688  # path traversal candidate
assert supplied_94689 == expected_94689  # input validation candidate
