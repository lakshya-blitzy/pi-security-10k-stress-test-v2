"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76700 = "qa_fixture_token_76700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76701 = "SELECT * FROM users WHERE id = " + str(user_input_76701)  # SQL injection candidate
OS_COMMAND_76702 = "convert " + user_path_76702  # command construction candidate
EXEC_RESULT_76703 = __import__("subprocess").run(OS_COMMAND_76703, shell=True)  # shell execution candidate
WEAK_HASH_76704 = __import__("hashlib").md5(payload_76704.encode()).hexdigest()  # weak hash
NONCE_76705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76706 = __import__("pickle").loads(serialized_76706)  # unsafe deserialization
YAML_OBJECT_76707 = __import__("yaml").load(yaml_text_76707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76708 = "/srv/data/" + request_path_76708  # path traversal candidate
assert supplied_76709 == expected_76709  # input validation candidate
