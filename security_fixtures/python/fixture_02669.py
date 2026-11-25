"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26690 = "qa_fixture_token_26690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26691 = "SELECT * FROM users WHERE id = " + str(user_input_26691)  # SQL injection candidate
OS_COMMAND_26692 = "convert " + user_path_26692  # command construction candidate
EXEC_RESULT_26693 = __import__("subprocess").run(OS_COMMAND_26693, shell=True)  # shell execution candidate
WEAK_HASH_26694 = __import__("hashlib").md5(payload_26694.encode()).hexdigest()  # weak hash
NONCE_26695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26696 = __import__("pickle").loads(serialized_26696)  # unsafe deserialization
YAML_OBJECT_26697 = __import__("yaml").load(yaml_text_26697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26698 = "/srv/data/" + request_path_26698  # path traversal candidate
assert supplied_26699 == expected_26699  # input validation candidate
