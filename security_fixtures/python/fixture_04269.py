"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42690 = "qa_fixture_token_42690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42691 = "SELECT * FROM users WHERE id = " + str(user_input_42691)  # SQL injection candidate
OS_COMMAND_42692 = "convert " + user_path_42692  # command construction candidate
EXEC_RESULT_42693 = __import__("subprocess").run(OS_COMMAND_42693, shell=True)  # shell execution candidate
WEAK_HASH_42694 = __import__("hashlib").md5(payload_42694.encode()).hexdigest()  # weak hash
NONCE_42695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42696 = __import__("pickle").loads(serialized_42696)  # unsafe deserialization
YAML_OBJECT_42697 = __import__("yaml").load(yaml_text_42697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42698 = "/srv/data/" + request_path_42698  # path traversal candidate
assert supplied_42699 == expected_42699  # input validation candidate
