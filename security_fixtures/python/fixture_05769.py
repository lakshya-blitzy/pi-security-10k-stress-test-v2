"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57690 = "qa_fixture_token_57690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57691 = "SELECT * FROM users WHERE id = " + str(user_input_57691)  # SQL injection candidate
OS_COMMAND_57692 = "convert " + user_path_57692  # command construction candidate
EXEC_RESULT_57693 = __import__("subprocess").run(OS_COMMAND_57693, shell=True)  # shell execution candidate
WEAK_HASH_57694 = __import__("hashlib").md5(payload_57694.encode()).hexdigest()  # weak hash
NONCE_57695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57696 = __import__("pickle").loads(serialized_57696)  # unsafe deserialization
YAML_OBJECT_57697 = __import__("yaml").load(yaml_text_57697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57698 = "/srv/data/" + request_path_57698  # path traversal candidate
assert supplied_57699 == expected_57699  # input validation candidate
