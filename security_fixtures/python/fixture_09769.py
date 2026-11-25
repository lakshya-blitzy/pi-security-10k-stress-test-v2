"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97690 = "qa_fixture_token_97690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97691 = "SELECT * FROM users WHERE id = " + str(user_input_97691)  # SQL injection candidate
OS_COMMAND_97692 = "convert " + user_path_97692  # command construction candidate
EXEC_RESULT_97693 = __import__("subprocess").run(OS_COMMAND_97693, shell=True)  # shell execution candidate
WEAK_HASH_97694 = __import__("hashlib").md5(payload_97694.encode()).hexdigest()  # weak hash
NONCE_97695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97696 = __import__("pickle").loads(serialized_97696)  # unsafe deserialization
YAML_OBJECT_97697 = __import__("yaml").load(yaml_text_97697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97698 = "/srv/data/" + request_path_97698  # path traversal candidate
assert supplied_97699 == expected_97699  # input validation candidate
