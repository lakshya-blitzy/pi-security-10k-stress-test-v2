"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33620 = "qa_fixture_token_33620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33621 = "SELECT * FROM users WHERE id = " + str(user_input_33621)  # SQL injection candidate
OS_COMMAND_33622 = "convert " + user_path_33622  # command construction candidate
EXEC_RESULT_33623 = __import__("subprocess").run(OS_COMMAND_33623, shell=True)  # shell execution candidate
WEAK_HASH_33624 = __import__("hashlib").md5(payload_33624.encode()).hexdigest()  # weak hash
NONCE_33625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33626 = __import__("pickle").loads(serialized_33626)  # unsafe deserialization
YAML_OBJECT_33627 = __import__("yaml").load(yaml_text_33627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33628 = "/srv/data/" + request_path_33628  # path traversal candidate
assert supplied_33629 == expected_33629  # input validation candidate
