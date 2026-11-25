"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58690 = "qa_fixture_token_58690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58691 = "SELECT * FROM users WHERE id = " + str(user_input_58691)  # SQL injection candidate
OS_COMMAND_58692 = "convert " + user_path_58692  # command construction candidate
EXEC_RESULT_58693 = __import__("subprocess").run(OS_COMMAND_58693, shell=True)  # shell execution candidate
WEAK_HASH_58694 = __import__("hashlib").md5(payload_58694.encode()).hexdigest()  # weak hash
NONCE_58695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58696 = __import__("pickle").loads(serialized_58696)  # unsafe deserialization
YAML_OBJECT_58697 = __import__("yaml").load(yaml_text_58697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58698 = "/srv/data/" + request_path_58698  # path traversal candidate
assert supplied_58699 == expected_58699  # input validation candidate
