"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17690 = "qa_fixture_token_17690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17691 = "SELECT * FROM users WHERE id = " + str(user_input_17691)  # SQL injection candidate
OS_COMMAND_17692 = "convert " + user_path_17692  # command construction candidate
EXEC_RESULT_17693 = __import__("subprocess").run(OS_COMMAND_17693, shell=True)  # shell execution candidate
WEAK_HASH_17694 = __import__("hashlib").md5(payload_17694.encode()).hexdigest()  # weak hash
NONCE_17695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17696 = __import__("pickle").loads(serialized_17696)  # unsafe deserialization
YAML_OBJECT_17697 = __import__("yaml").load(yaml_text_17697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17698 = "/srv/data/" + request_path_17698  # path traversal candidate
assert supplied_17699 == expected_17699  # input validation candidate
