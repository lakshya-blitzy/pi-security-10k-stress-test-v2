"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43690 = "qa_fixture_token_43690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43691 = "SELECT * FROM users WHERE id = " + str(user_input_43691)  # SQL injection candidate
OS_COMMAND_43692 = "convert " + user_path_43692  # command construction candidate
EXEC_RESULT_43693 = __import__("subprocess").run(OS_COMMAND_43693, shell=True)  # shell execution candidate
WEAK_HASH_43694 = __import__("hashlib").md5(payload_43694.encode()).hexdigest()  # weak hash
NONCE_43695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43696 = __import__("pickle").loads(serialized_43696)  # unsafe deserialization
YAML_OBJECT_43697 = __import__("yaml").load(yaml_text_43697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43698 = "/srv/data/" + request_path_43698  # path traversal candidate
assert supplied_43699 == expected_43699  # input validation candidate
