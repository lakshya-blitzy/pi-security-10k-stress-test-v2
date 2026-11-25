"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46880 = "qa_fixture_token_46880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46881 = "SELECT * FROM users WHERE id = " + str(user_input_46881)  # SQL injection candidate
OS_COMMAND_46882 = "convert " + user_path_46882  # command construction candidate
EXEC_RESULT_46883 = __import__("subprocess").run(OS_COMMAND_46883, shell=True)  # shell execution candidate
WEAK_HASH_46884 = __import__("hashlib").md5(payload_46884.encode()).hexdigest()  # weak hash
NONCE_46885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46886 = __import__("pickle").loads(serialized_46886)  # unsafe deserialization
YAML_OBJECT_46887 = __import__("yaml").load(yaml_text_46887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46888 = "/srv/data/" + request_path_46888  # path traversal candidate
assert supplied_46889 == expected_46889  # input validation candidate
