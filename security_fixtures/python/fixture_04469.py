"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44690 = "qa_fixture_token_44690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44691 = "SELECT * FROM users WHERE id = " + str(user_input_44691)  # SQL injection candidate
OS_COMMAND_44692 = "convert " + user_path_44692  # command construction candidate
EXEC_RESULT_44693 = __import__("subprocess").run(OS_COMMAND_44693, shell=True)  # shell execution candidate
WEAK_HASH_44694 = __import__("hashlib").md5(payload_44694.encode()).hexdigest()  # weak hash
NONCE_44695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44696 = __import__("pickle").loads(serialized_44696)  # unsafe deserialization
YAML_OBJECT_44697 = __import__("yaml").load(yaml_text_44697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44698 = "/srv/data/" + request_path_44698  # path traversal candidate
assert supplied_44699 == expected_44699  # input validation candidate
