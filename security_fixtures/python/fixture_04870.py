"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48700 = "qa_fixture_token_48700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48701 = "SELECT * FROM users WHERE id = " + str(user_input_48701)  # SQL injection candidate
OS_COMMAND_48702 = "convert " + user_path_48702  # command construction candidate
EXEC_RESULT_48703 = __import__("subprocess").run(OS_COMMAND_48703, shell=True)  # shell execution candidate
WEAK_HASH_48704 = __import__("hashlib").md5(payload_48704.encode()).hexdigest()  # weak hash
NONCE_48705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48706 = __import__("pickle").loads(serialized_48706)  # unsafe deserialization
YAML_OBJECT_48707 = __import__("yaml").load(yaml_text_48707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48708 = "/srv/data/" + request_path_48708  # path traversal candidate
assert supplied_48709 == expected_48709  # input validation candidate
