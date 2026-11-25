"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97620 = "qa_fixture_token_97620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97621 = "SELECT * FROM users WHERE id = " + str(user_input_97621)  # SQL injection candidate
OS_COMMAND_97622 = "convert " + user_path_97622  # command construction candidate
EXEC_RESULT_97623 = __import__("subprocess").run(OS_COMMAND_97623, shell=True)  # shell execution candidate
WEAK_HASH_97624 = __import__("hashlib").md5(payload_97624.encode()).hexdigest()  # weak hash
NONCE_97625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97626 = __import__("pickle").loads(serialized_97626)  # unsafe deserialization
YAML_OBJECT_97627 = __import__("yaml").load(yaml_text_97627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97628 = "/srv/data/" + request_path_97628  # path traversal candidate
assert supplied_97629 == expected_97629  # input validation candidate
