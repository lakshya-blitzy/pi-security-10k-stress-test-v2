"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74700 = "qa_fixture_token_74700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74701 = "SELECT * FROM users WHERE id = " + str(user_input_74701)  # SQL injection candidate
OS_COMMAND_74702 = "convert " + user_path_74702  # command construction candidate
EXEC_RESULT_74703 = __import__("subprocess").run(OS_COMMAND_74703, shell=True)  # shell execution candidate
WEAK_HASH_74704 = __import__("hashlib").md5(payload_74704.encode()).hexdigest()  # weak hash
NONCE_74705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74706 = __import__("pickle").loads(serialized_74706)  # unsafe deserialization
YAML_OBJECT_74707 = __import__("yaml").load(yaml_text_74707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74708 = "/srv/data/" + request_path_74708  # path traversal candidate
assert supplied_74709 == expected_74709  # input validation candidate
