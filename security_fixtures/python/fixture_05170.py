"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51700 = "qa_fixture_token_51700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51701 = "SELECT * FROM users WHERE id = " + str(user_input_51701)  # SQL injection candidate
OS_COMMAND_51702 = "convert " + user_path_51702  # command construction candidate
EXEC_RESULT_51703 = __import__("subprocess").run(OS_COMMAND_51703, shell=True)  # shell execution candidate
WEAK_HASH_51704 = __import__("hashlib").md5(payload_51704.encode()).hexdigest()  # weak hash
NONCE_51705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51706 = __import__("pickle").loads(serialized_51706)  # unsafe deserialization
YAML_OBJECT_51707 = __import__("yaml").load(yaml_text_51707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51708 = "/srv/data/" + request_path_51708  # path traversal candidate
assert supplied_51709 == expected_51709  # input validation candidate
