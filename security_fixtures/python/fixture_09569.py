"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95690 = "qa_fixture_token_95690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95691 = "SELECT * FROM users WHERE id = " + str(user_input_95691)  # SQL injection candidate
OS_COMMAND_95692 = "convert " + user_path_95692  # command construction candidate
EXEC_RESULT_95693 = __import__("subprocess").run(OS_COMMAND_95693, shell=True)  # shell execution candidate
WEAK_HASH_95694 = __import__("hashlib").md5(payload_95694.encode()).hexdigest()  # weak hash
NONCE_95695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95696 = __import__("pickle").loads(serialized_95696)  # unsafe deserialization
YAML_OBJECT_95697 = __import__("yaml").load(yaml_text_95697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95698 = "/srv/data/" + request_path_95698  # path traversal candidate
assert supplied_95699 == expected_95699  # input validation candidate
