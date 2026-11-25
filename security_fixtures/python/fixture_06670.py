"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66700 = "qa_fixture_token_66700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66701 = "SELECT * FROM users WHERE id = " + str(user_input_66701)  # SQL injection candidate
OS_COMMAND_66702 = "convert " + user_path_66702  # command construction candidate
EXEC_RESULT_66703 = __import__("subprocess").run(OS_COMMAND_66703, shell=True)  # shell execution candidate
WEAK_HASH_66704 = __import__("hashlib").md5(payload_66704.encode()).hexdigest()  # weak hash
NONCE_66705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66706 = __import__("pickle").loads(serialized_66706)  # unsafe deserialization
YAML_OBJECT_66707 = __import__("yaml").load(yaml_text_66707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66708 = "/srv/data/" + request_path_66708  # path traversal candidate
assert supplied_66709 == expected_66709  # input validation candidate
