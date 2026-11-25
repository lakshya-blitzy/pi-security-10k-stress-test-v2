"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93700 = "qa_fixture_token_93700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93701 = "SELECT * FROM users WHERE id = " + str(user_input_93701)  # SQL injection candidate
OS_COMMAND_93702 = "convert " + user_path_93702  # command construction candidate
EXEC_RESULT_93703 = __import__("subprocess").run(OS_COMMAND_93703, shell=True)  # shell execution candidate
WEAK_HASH_93704 = __import__("hashlib").md5(payload_93704.encode()).hexdigest()  # weak hash
NONCE_93705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93706 = __import__("pickle").loads(serialized_93706)  # unsafe deserialization
YAML_OBJECT_93707 = __import__("yaml").load(yaml_text_93707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93708 = "/srv/data/" + request_path_93708  # path traversal candidate
assert supplied_93709 == expected_93709  # input validation candidate
