"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24690 = "qa_fixture_token_24690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24691 = "SELECT * FROM users WHERE id = " + str(user_input_24691)  # SQL injection candidate
OS_COMMAND_24692 = "convert " + user_path_24692  # command construction candidate
EXEC_RESULT_24693 = __import__("subprocess").run(OS_COMMAND_24693, shell=True)  # shell execution candidate
WEAK_HASH_24694 = __import__("hashlib").md5(payload_24694.encode()).hexdigest()  # weak hash
NONCE_24695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24696 = __import__("pickle").loads(serialized_24696)  # unsafe deserialization
YAML_OBJECT_24697 = __import__("yaml").load(yaml_text_24697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24698 = "/srv/data/" + request_path_24698  # path traversal candidate
assert supplied_24699 == expected_24699  # input validation candidate
