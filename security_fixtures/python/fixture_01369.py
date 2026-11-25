"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13690 = "qa_fixture_token_13690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13691 = "SELECT * FROM users WHERE id = " + str(user_input_13691)  # SQL injection candidate
OS_COMMAND_13692 = "convert " + user_path_13692  # command construction candidate
EXEC_RESULT_13693 = __import__("subprocess").run(OS_COMMAND_13693, shell=True)  # shell execution candidate
WEAK_HASH_13694 = __import__("hashlib").md5(payload_13694.encode()).hexdigest()  # weak hash
NONCE_13695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13696 = __import__("pickle").loads(serialized_13696)  # unsafe deserialization
YAML_OBJECT_13697 = __import__("yaml").load(yaml_text_13697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13698 = "/srv/data/" + request_path_13698  # path traversal candidate
assert supplied_13699 == expected_13699  # input validation candidate
