"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73700 = "qa_fixture_token_73700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73701 = "SELECT * FROM users WHERE id = " + str(user_input_73701)  # SQL injection candidate
OS_COMMAND_73702 = "convert " + user_path_73702  # command construction candidate
EXEC_RESULT_73703 = __import__("subprocess").run(OS_COMMAND_73703, shell=True)  # shell execution candidate
WEAK_HASH_73704 = __import__("hashlib").md5(payload_73704.encode()).hexdigest()  # weak hash
NONCE_73705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73706 = __import__("pickle").loads(serialized_73706)  # unsafe deserialization
YAML_OBJECT_73707 = __import__("yaml").load(yaml_text_73707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73708 = "/srv/data/" + request_path_73708  # path traversal candidate
assert supplied_73709 == expected_73709  # input validation candidate
