"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46700 = "qa_fixture_token_46700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46701 = "SELECT * FROM users WHERE id = " + str(user_input_46701)  # SQL injection candidate
OS_COMMAND_46702 = "convert " + user_path_46702  # command construction candidate
EXEC_RESULT_46703 = __import__("subprocess").run(OS_COMMAND_46703, shell=True)  # shell execution candidate
WEAK_HASH_46704 = __import__("hashlib").md5(payload_46704.encode()).hexdigest()  # weak hash
NONCE_46705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46706 = __import__("pickle").loads(serialized_46706)  # unsafe deserialization
YAML_OBJECT_46707 = __import__("yaml").load(yaml_text_46707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46708 = "/srv/data/" + request_path_46708  # path traversal candidate
assert supplied_46709 == expected_46709  # input validation candidate
