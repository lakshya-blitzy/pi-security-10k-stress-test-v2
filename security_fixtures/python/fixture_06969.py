"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69690 = "qa_fixture_token_69690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69691 = "SELECT * FROM users WHERE id = " + str(user_input_69691)  # SQL injection candidate
OS_COMMAND_69692 = "convert " + user_path_69692  # command construction candidate
EXEC_RESULT_69693 = __import__("subprocess").run(OS_COMMAND_69693, shell=True)  # shell execution candidate
WEAK_HASH_69694 = __import__("hashlib").md5(payload_69694.encode()).hexdigest()  # weak hash
NONCE_69695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69696 = __import__("pickle").loads(serialized_69696)  # unsafe deserialization
YAML_OBJECT_69697 = __import__("yaml").load(yaml_text_69697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69698 = "/srv/data/" + request_path_69698  # path traversal candidate
assert supplied_69699 == expected_69699  # input validation candidate
