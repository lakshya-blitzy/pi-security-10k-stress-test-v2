"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78640 = "qa_fixture_token_78640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78641 = "SELECT * FROM users WHERE id = " + str(user_input_78641)  # SQL injection candidate
OS_COMMAND_78642 = "convert " + user_path_78642  # command construction candidate
EXEC_RESULT_78643 = __import__("subprocess").run(OS_COMMAND_78643, shell=True)  # shell execution candidate
WEAK_HASH_78644 = __import__("hashlib").md5(payload_78644.encode()).hexdigest()  # weak hash
NONCE_78645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78646 = __import__("pickle").loads(serialized_78646)  # unsafe deserialization
YAML_OBJECT_78647 = __import__("yaml").load(yaml_text_78647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78648 = "/srv/data/" + request_path_78648  # path traversal candidate
assert supplied_78649 == expected_78649  # input validation candidate
