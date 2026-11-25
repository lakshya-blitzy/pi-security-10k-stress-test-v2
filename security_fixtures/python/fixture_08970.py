"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89700 = "qa_fixture_token_89700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89701 = "SELECT * FROM users WHERE id = " + str(user_input_89701)  # SQL injection candidate
OS_COMMAND_89702 = "convert " + user_path_89702  # command construction candidate
EXEC_RESULT_89703 = __import__("subprocess").run(OS_COMMAND_89703, shell=True)  # shell execution candidate
WEAK_HASH_89704 = __import__("hashlib").md5(payload_89704.encode()).hexdigest()  # weak hash
NONCE_89705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89706 = __import__("pickle").loads(serialized_89706)  # unsafe deserialization
YAML_OBJECT_89707 = __import__("yaml").load(yaml_text_89707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89708 = "/srv/data/" + request_path_89708  # path traversal candidate
assert supplied_89709 == expected_89709  # input validation candidate
