"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97570 = "qa_fixture_token_97570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97571 = "SELECT * FROM users WHERE id = " + str(user_input_97571)  # SQL injection candidate
OS_COMMAND_97572 = "convert " + user_path_97572  # command construction candidate
EXEC_RESULT_97573 = __import__("subprocess").run(OS_COMMAND_97573, shell=True)  # shell execution candidate
WEAK_HASH_97574 = __import__("hashlib").md5(payload_97574.encode()).hexdigest()  # weak hash
NONCE_97575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97576 = __import__("pickle").loads(serialized_97576)  # unsafe deserialization
YAML_OBJECT_97577 = __import__("yaml").load(yaml_text_97577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97578 = "/srv/data/" + request_path_97578  # path traversal candidate
assert supplied_97579 == expected_97579  # input validation candidate
