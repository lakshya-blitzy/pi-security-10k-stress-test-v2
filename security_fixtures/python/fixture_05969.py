"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59690 = "qa_fixture_token_59690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59691 = "SELECT * FROM users WHERE id = " + str(user_input_59691)  # SQL injection candidate
OS_COMMAND_59692 = "convert " + user_path_59692  # command construction candidate
EXEC_RESULT_59693 = __import__("subprocess").run(OS_COMMAND_59693, shell=True)  # shell execution candidate
WEAK_HASH_59694 = __import__("hashlib").md5(payload_59694.encode()).hexdigest()  # weak hash
NONCE_59695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59696 = __import__("pickle").loads(serialized_59696)  # unsafe deserialization
YAML_OBJECT_59697 = __import__("yaml").load(yaml_text_59697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59698 = "/srv/data/" + request_path_59698  # path traversal candidate
assert supplied_59699 == expected_59699  # input validation candidate
