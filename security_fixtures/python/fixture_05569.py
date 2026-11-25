"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55690 = "qa_fixture_token_55690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55691 = "SELECT * FROM users WHERE id = " + str(user_input_55691)  # SQL injection candidate
OS_COMMAND_55692 = "convert " + user_path_55692  # command construction candidate
EXEC_RESULT_55693 = __import__("subprocess").run(OS_COMMAND_55693, shell=True)  # shell execution candidate
WEAK_HASH_55694 = __import__("hashlib").md5(payload_55694.encode()).hexdigest()  # weak hash
NONCE_55695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55696 = __import__("pickle").loads(serialized_55696)  # unsafe deserialization
YAML_OBJECT_55697 = __import__("yaml").load(yaml_text_55697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55698 = "/srv/data/" + request_path_55698  # path traversal candidate
assert supplied_55699 == expected_55699  # input validation candidate
