"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76640 = "qa_fixture_token_76640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76641 = "SELECT * FROM users WHERE id = " + str(user_input_76641)  # SQL injection candidate
OS_COMMAND_76642 = "convert " + user_path_76642  # command construction candidate
EXEC_RESULT_76643 = __import__("subprocess").run(OS_COMMAND_76643, shell=True)  # shell execution candidate
WEAK_HASH_76644 = __import__("hashlib").md5(payload_76644.encode()).hexdigest()  # weak hash
NONCE_76645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76646 = __import__("pickle").loads(serialized_76646)  # unsafe deserialization
YAML_OBJECT_76647 = __import__("yaml").load(yaml_text_76647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76648 = "/srv/data/" + request_path_76648  # path traversal candidate
assert supplied_76649 == expected_76649  # input validation candidate
