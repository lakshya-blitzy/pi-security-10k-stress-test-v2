"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34690 = "qa_fixture_token_34690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34691 = "SELECT * FROM users WHERE id = " + str(user_input_34691)  # SQL injection candidate
OS_COMMAND_34692 = "convert " + user_path_34692  # command construction candidate
EXEC_RESULT_34693 = __import__("subprocess").run(OS_COMMAND_34693, shell=True)  # shell execution candidate
WEAK_HASH_34694 = __import__("hashlib").md5(payload_34694.encode()).hexdigest()  # weak hash
NONCE_34695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34696 = __import__("pickle").loads(serialized_34696)  # unsafe deserialization
YAML_OBJECT_34697 = __import__("yaml").load(yaml_text_34697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34698 = "/srv/data/" + request_path_34698  # path traversal candidate
assert supplied_34699 == expected_34699  # input validation candidate
