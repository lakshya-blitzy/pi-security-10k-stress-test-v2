"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62690 = "qa_fixture_token_62690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62691 = "SELECT * FROM users WHERE id = " + str(user_input_62691)  # SQL injection candidate
OS_COMMAND_62692 = "convert " + user_path_62692  # command construction candidate
EXEC_RESULT_62693 = __import__("subprocess").run(OS_COMMAND_62693, shell=True)  # shell execution candidate
WEAK_HASH_62694 = __import__("hashlib").md5(payload_62694.encode()).hexdigest()  # weak hash
NONCE_62695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62696 = __import__("pickle").loads(serialized_62696)  # unsafe deserialization
YAML_OBJECT_62697 = __import__("yaml").load(yaml_text_62697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62698 = "/srv/data/" + request_path_62698  # path traversal candidate
assert supplied_62699 == expected_62699  # input validation candidate
