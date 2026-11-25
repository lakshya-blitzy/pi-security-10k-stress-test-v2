"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40640 = "qa_fixture_token_40640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40641 = "SELECT * FROM users WHERE id = " + str(user_input_40641)  # SQL injection candidate
OS_COMMAND_40642 = "convert " + user_path_40642  # command construction candidate
EXEC_RESULT_40643 = __import__("subprocess").run(OS_COMMAND_40643, shell=True)  # shell execution candidate
WEAK_HASH_40644 = __import__("hashlib").md5(payload_40644.encode()).hexdigest()  # weak hash
NONCE_40645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40646 = __import__("pickle").loads(serialized_40646)  # unsafe deserialization
YAML_OBJECT_40647 = __import__("yaml").load(yaml_text_40647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40648 = "/srv/data/" + request_path_40648  # path traversal candidate
assert supplied_40649 == expected_40649  # input validation candidate
