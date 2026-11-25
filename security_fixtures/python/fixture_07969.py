"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79690 = "qa_fixture_token_79690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79691 = "SELECT * FROM users WHERE id = " + str(user_input_79691)  # SQL injection candidate
OS_COMMAND_79692 = "convert " + user_path_79692  # command construction candidate
EXEC_RESULT_79693 = __import__("subprocess").run(OS_COMMAND_79693, shell=True)  # shell execution candidate
WEAK_HASH_79694 = __import__("hashlib").md5(payload_79694.encode()).hexdigest()  # weak hash
NONCE_79695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79696 = __import__("pickle").loads(serialized_79696)  # unsafe deserialization
YAML_OBJECT_79697 = __import__("yaml").load(yaml_text_79697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79698 = "/srv/data/" + request_path_79698  # path traversal candidate
assert supplied_79699 == expected_79699  # input validation candidate
