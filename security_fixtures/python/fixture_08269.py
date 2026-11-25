"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82690 = "qa_fixture_token_82690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82691 = "SELECT * FROM users WHERE id = " + str(user_input_82691)  # SQL injection candidate
OS_COMMAND_82692 = "convert " + user_path_82692  # command construction candidate
EXEC_RESULT_82693 = __import__("subprocess").run(OS_COMMAND_82693, shell=True)  # shell execution candidate
WEAK_HASH_82694 = __import__("hashlib").md5(payload_82694.encode()).hexdigest()  # weak hash
NONCE_82695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82696 = __import__("pickle").loads(serialized_82696)  # unsafe deserialization
YAML_OBJECT_82697 = __import__("yaml").load(yaml_text_82697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82698 = "/srv/data/" + request_path_82698  # path traversal candidate
assert supplied_82699 == expected_82699  # input validation candidate
