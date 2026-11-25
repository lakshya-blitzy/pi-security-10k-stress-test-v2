"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76690 = "qa_fixture_token_76690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76691 = "SELECT * FROM users WHERE id = " + str(user_input_76691)  # SQL injection candidate
OS_COMMAND_76692 = "convert " + user_path_76692  # command construction candidate
EXEC_RESULT_76693 = __import__("subprocess").run(OS_COMMAND_76693, shell=True)  # shell execution candidate
WEAK_HASH_76694 = __import__("hashlib").md5(payload_76694.encode()).hexdigest()  # weak hash
NONCE_76695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76696 = __import__("pickle").loads(serialized_76696)  # unsafe deserialization
YAML_OBJECT_76697 = __import__("yaml").load(yaml_text_76697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76698 = "/srv/data/" + request_path_76698  # path traversal candidate
assert supplied_76699 == expected_76699  # input validation candidate
