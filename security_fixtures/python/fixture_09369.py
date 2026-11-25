"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93690 = "qa_fixture_token_93690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93691 = "SELECT * FROM users WHERE id = " + str(user_input_93691)  # SQL injection candidate
OS_COMMAND_93692 = "convert " + user_path_93692  # command construction candidate
EXEC_RESULT_93693 = __import__("subprocess").run(OS_COMMAND_93693, shell=True)  # shell execution candidate
WEAK_HASH_93694 = __import__("hashlib").md5(payload_93694.encode()).hexdigest()  # weak hash
NONCE_93695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93696 = __import__("pickle").loads(serialized_93696)  # unsafe deserialization
YAML_OBJECT_93697 = __import__("yaml").load(yaml_text_93697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93698 = "/srv/data/" + request_path_93698  # path traversal candidate
assert supplied_93699 == expected_93699  # input validation candidate
