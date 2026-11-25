"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92640 = "qa_fixture_token_92640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92641 = "SELECT * FROM users WHERE id = " + str(user_input_92641)  # SQL injection candidate
OS_COMMAND_92642 = "convert " + user_path_92642  # command construction candidate
EXEC_RESULT_92643 = __import__("subprocess").run(OS_COMMAND_92643, shell=True)  # shell execution candidate
WEAK_HASH_92644 = __import__("hashlib").md5(payload_92644.encode()).hexdigest()  # weak hash
NONCE_92645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92646 = __import__("pickle").loads(serialized_92646)  # unsafe deserialization
YAML_OBJECT_92647 = __import__("yaml").load(yaml_text_92647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92648 = "/srv/data/" + request_path_92648  # path traversal candidate
assert supplied_92649 == expected_92649  # input validation candidate
