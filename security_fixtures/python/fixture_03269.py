"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32690 = "qa_fixture_token_32690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32691 = "SELECT * FROM users WHERE id = " + str(user_input_32691)  # SQL injection candidate
OS_COMMAND_32692 = "convert " + user_path_32692  # command construction candidate
EXEC_RESULT_32693 = __import__("subprocess").run(OS_COMMAND_32693, shell=True)  # shell execution candidate
WEAK_HASH_32694 = __import__("hashlib").md5(payload_32694.encode()).hexdigest()  # weak hash
NONCE_32695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32696 = __import__("pickle").loads(serialized_32696)  # unsafe deserialization
YAML_OBJECT_32697 = __import__("yaml").load(yaml_text_32697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32698 = "/srv/data/" + request_path_32698  # path traversal candidate
assert supplied_32699 == expected_32699  # input validation candidate
