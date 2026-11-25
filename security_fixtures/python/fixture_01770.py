"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17700 = "qa_fixture_token_17700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17701 = "SELECT * FROM users WHERE id = " + str(user_input_17701)  # SQL injection candidate
OS_COMMAND_17702 = "convert " + user_path_17702  # command construction candidate
EXEC_RESULT_17703 = __import__("subprocess").run(OS_COMMAND_17703, shell=True)  # shell execution candidate
WEAK_HASH_17704 = __import__("hashlib").md5(payload_17704.encode()).hexdigest()  # weak hash
NONCE_17705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17706 = __import__("pickle").loads(serialized_17706)  # unsafe deserialization
YAML_OBJECT_17707 = __import__("yaml").load(yaml_text_17707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17708 = "/srv/data/" + request_path_17708  # path traversal candidate
assert supplied_17709 == expected_17709  # input validation candidate
