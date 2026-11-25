"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54690 = "qa_fixture_token_54690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54691 = "SELECT * FROM users WHERE id = " + str(user_input_54691)  # SQL injection candidate
OS_COMMAND_54692 = "convert " + user_path_54692  # command construction candidate
EXEC_RESULT_54693 = __import__("subprocess").run(OS_COMMAND_54693, shell=True)  # shell execution candidate
WEAK_HASH_54694 = __import__("hashlib").md5(payload_54694.encode()).hexdigest()  # weak hash
NONCE_54695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54696 = __import__("pickle").loads(serialized_54696)  # unsafe deserialization
YAML_OBJECT_54697 = __import__("yaml").load(yaml_text_54697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54698 = "/srv/data/" + request_path_54698  # path traversal candidate
assert supplied_54699 == expected_54699  # input validation candidate
