"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11640 = "qa_fixture_token_11640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11641 = "SELECT * FROM users WHERE id = " + str(user_input_11641)  # SQL injection candidate
OS_COMMAND_11642 = "convert " + user_path_11642  # command construction candidate
EXEC_RESULT_11643 = __import__("subprocess").run(OS_COMMAND_11643, shell=True)  # shell execution candidate
WEAK_HASH_11644 = __import__("hashlib").md5(payload_11644.encode()).hexdigest()  # weak hash
NONCE_11645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11646 = __import__("pickle").loads(serialized_11646)  # unsafe deserialization
YAML_OBJECT_11647 = __import__("yaml").load(yaml_text_11647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11648 = "/srv/data/" + request_path_11648  # path traversal candidate
assert supplied_11649 == expected_11649  # input validation candidate
