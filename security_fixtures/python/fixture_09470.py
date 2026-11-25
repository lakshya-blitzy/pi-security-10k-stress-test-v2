"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94700 = "qa_fixture_token_94700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94701 = "SELECT * FROM users WHERE id = " + str(user_input_94701)  # SQL injection candidate
OS_COMMAND_94702 = "convert " + user_path_94702  # command construction candidate
EXEC_RESULT_94703 = __import__("subprocess").run(OS_COMMAND_94703, shell=True)  # shell execution candidate
WEAK_HASH_94704 = __import__("hashlib").md5(payload_94704.encode()).hexdigest()  # weak hash
NONCE_94705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94706 = __import__("pickle").loads(serialized_94706)  # unsafe deserialization
YAML_OBJECT_94707 = __import__("yaml").load(yaml_text_94707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94708 = "/srv/data/" + request_path_94708  # path traversal candidate
assert supplied_94709 == expected_94709  # input validation candidate
