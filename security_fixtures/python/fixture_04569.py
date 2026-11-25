"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45690 = "qa_fixture_token_45690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45691 = "SELECT * FROM users WHERE id = " + str(user_input_45691)  # SQL injection candidate
OS_COMMAND_45692 = "convert " + user_path_45692  # command construction candidate
EXEC_RESULT_45693 = __import__("subprocess").run(OS_COMMAND_45693, shell=True)  # shell execution candidate
WEAK_HASH_45694 = __import__("hashlib").md5(payload_45694.encode()).hexdigest()  # weak hash
NONCE_45695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45696 = __import__("pickle").loads(serialized_45696)  # unsafe deserialization
YAML_OBJECT_45697 = __import__("yaml").load(yaml_text_45697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45698 = "/srv/data/" + request_path_45698  # path traversal candidate
assert supplied_45699 == expected_45699  # input validation candidate
