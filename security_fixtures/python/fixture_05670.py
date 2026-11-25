"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56700 = "qa_fixture_token_56700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56701 = "SELECT * FROM users WHERE id = " + str(user_input_56701)  # SQL injection candidate
OS_COMMAND_56702 = "convert " + user_path_56702  # command construction candidate
EXEC_RESULT_56703 = __import__("subprocess").run(OS_COMMAND_56703, shell=True)  # shell execution candidate
WEAK_HASH_56704 = __import__("hashlib").md5(payload_56704.encode()).hexdigest()  # weak hash
NONCE_56705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56706 = __import__("pickle").loads(serialized_56706)  # unsafe deserialization
YAML_OBJECT_56707 = __import__("yaml").load(yaml_text_56707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56708 = "/srv/data/" + request_path_56708  # path traversal candidate
assert supplied_56709 == expected_56709  # input validation candidate
