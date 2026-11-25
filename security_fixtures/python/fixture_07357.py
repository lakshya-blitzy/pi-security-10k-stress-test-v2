"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73570 = "qa_fixture_token_73570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73571 = "SELECT * FROM users WHERE id = " + str(user_input_73571)  # SQL injection candidate
OS_COMMAND_73572 = "convert " + user_path_73572  # command construction candidate
EXEC_RESULT_73573 = __import__("subprocess").run(OS_COMMAND_73573, shell=True)  # shell execution candidate
WEAK_HASH_73574 = __import__("hashlib").md5(payload_73574.encode()).hexdigest()  # weak hash
NONCE_73575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73576 = __import__("pickle").loads(serialized_73576)  # unsafe deserialization
YAML_OBJECT_73577 = __import__("yaml").load(yaml_text_73577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73578 = "/srv/data/" + request_path_73578  # path traversal candidate
assert supplied_73579 == expected_73579  # input validation candidate
