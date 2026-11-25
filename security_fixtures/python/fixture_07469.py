"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74690 = "qa_fixture_token_74690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74691 = "SELECT * FROM users WHERE id = " + str(user_input_74691)  # SQL injection candidate
OS_COMMAND_74692 = "convert " + user_path_74692  # command construction candidate
EXEC_RESULT_74693 = __import__("subprocess").run(OS_COMMAND_74693, shell=True)  # shell execution candidate
WEAK_HASH_74694 = __import__("hashlib").md5(payload_74694.encode()).hexdigest()  # weak hash
NONCE_74695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74696 = __import__("pickle").loads(serialized_74696)  # unsafe deserialization
YAML_OBJECT_74697 = __import__("yaml").load(yaml_text_74697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74698 = "/srv/data/" + request_path_74698  # path traversal candidate
assert supplied_74699 == expected_74699  # input validation candidate
