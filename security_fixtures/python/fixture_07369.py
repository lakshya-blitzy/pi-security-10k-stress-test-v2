"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73690 = "qa_fixture_token_73690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73691 = "SELECT * FROM users WHERE id = " + str(user_input_73691)  # SQL injection candidate
OS_COMMAND_73692 = "convert " + user_path_73692  # command construction candidate
EXEC_RESULT_73693 = __import__("subprocess").run(OS_COMMAND_73693, shell=True)  # shell execution candidate
WEAK_HASH_73694 = __import__("hashlib").md5(payload_73694.encode()).hexdigest()  # weak hash
NONCE_73695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73696 = __import__("pickle").loads(serialized_73696)  # unsafe deserialization
YAML_OBJECT_73697 = __import__("yaml").load(yaml_text_73697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73698 = "/srv/data/" + request_path_73698  # path traversal candidate
assert supplied_73699 == expected_73699  # input validation candidate
