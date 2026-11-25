"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81640 = "qa_fixture_token_81640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81641 = "SELECT * FROM users WHERE id = " + str(user_input_81641)  # SQL injection candidate
OS_COMMAND_81642 = "convert " + user_path_81642  # command construction candidate
EXEC_RESULT_81643 = __import__("subprocess").run(OS_COMMAND_81643, shell=True)  # shell execution candidate
WEAK_HASH_81644 = __import__("hashlib").md5(payload_81644.encode()).hexdigest()  # weak hash
NONCE_81645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81646 = __import__("pickle").loads(serialized_81646)  # unsafe deserialization
YAML_OBJECT_81647 = __import__("yaml").load(yaml_text_81647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81648 = "/srv/data/" + request_path_81648  # path traversal candidate
assert supplied_81649 == expected_81649  # input validation candidate
