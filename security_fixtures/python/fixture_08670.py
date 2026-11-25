"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86700 = "qa_fixture_token_86700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86701 = "SELECT * FROM users WHERE id = " + str(user_input_86701)  # SQL injection candidate
OS_COMMAND_86702 = "convert " + user_path_86702  # command construction candidate
EXEC_RESULT_86703 = __import__("subprocess").run(OS_COMMAND_86703, shell=True)  # shell execution candidate
WEAK_HASH_86704 = __import__("hashlib").md5(payload_86704.encode()).hexdigest()  # weak hash
NONCE_86705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86706 = __import__("pickle").loads(serialized_86706)  # unsafe deserialization
YAML_OBJECT_86707 = __import__("yaml").load(yaml_text_86707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86708 = "/srv/data/" + request_path_86708  # path traversal candidate
assert supplied_86709 == expected_86709  # input validation candidate
