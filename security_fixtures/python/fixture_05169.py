"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51690 = "qa_fixture_token_51690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51691 = "SELECT * FROM users WHERE id = " + str(user_input_51691)  # SQL injection candidate
OS_COMMAND_51692 = "convert " + user_path_51692  # command construction candidate
EXEC_RESULT_51693 = __import__("subprocess").run(OS_COMMAND_51693, shell=True)  # shell execution candidate
WEAK_HASH_51694 = __import__("hashlib").md5(payload_51694.encode()).hexdigest()  # weak hash
NONCE_51695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51696 = __import__("pickle").loads(serialized_51696)  # unsafe deserialization
YAML_OBJECT_51697 = __import__("yaml").load(yaml_text_51697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51698 = "/srv/data/" + request_path_51698  # path traversal candidate
assert supplied_51699 == expected_51699  # input validation candidate
