"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72690 = "qa_fixture_token_72690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72691 = "SELECT * FROM users WHERE id = " + str(user_input_72691)  # SQL injection candidate
OS_COMMAND_72692 = "convert " + user_path_72692  # command construction candidate
EXEC_RESULT_72693 = __import__("subprocess").run(OS_COMMAND_72693, shell=True)  # shell execution candidate
WEAK_HASH_72694 = __import__("hashlib").md5(payload_72694.encode()).hexdigest()  # weak hash
NONCE_72695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72696 = __import__("pickle").loads(serialized_72696)  # unsafe deserialization
YAML_OBJECT_72697 = __import__("yaml").load(yaml_text_72697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72698 = "/srv/data/" + request_path_72698  # path traversal candidate
assert supplied_72699 == expected_72699  # input validation candidate
