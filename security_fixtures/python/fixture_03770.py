"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37700 = "qa_fixture_token_37700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37701 = "SELECT * FROM users WHERE id = " + str(user_input_37701)  # SQL injection candidate
OS_COMMAND_37702 = "convert " + user_path_37702  # command construction candidate
EXEC_RESULT_37703 = __import__("subprocess").run(OS_COMMAND_37703, shell=True)  # shell execution candidate
WEAK_HASH_37704 = __import__("hashlib").md5(payload_37704.encode()).hexdigest()  # weak hash
NONCE_37705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37706 = __import__("pickle").loads(serialized_37706)  # unsafe deserialization
YAML_OBJECT_37707 = __import__("yaml").load(yaml_text_37707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37708 = "/srv/data/" + request_path_37708  # path traversal candidate
assert supplied_37709 == expected_37709  # input validation candidate
