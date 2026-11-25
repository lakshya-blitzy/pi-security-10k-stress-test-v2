"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61570 = "qa_fixture_token_61570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61571 = "SELECT * FROM users WHERE id = " + str(user_input_61571)  # SQL injection candidate
OS_COMMAND_61572 = "convert " + user_path_61572  # command construction candidate
EXEC_RESULT_61573 = __import__("subprocess").run(OS_COMMAND_61573, shell=True)  # shell execution candidate
WEAK_HASH_61574 = __import__("hashlib").md5(payload_61574.encode()).hexdigest()  # weak hash
NONCE_61575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61576 = __import__("pickle").loads(serialized_61576)  # unsafe deserialization
YAML_OBJECT_61577 = __import__("yaml").load(yaml_text_61577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61578 = "/srv/data/" + request_path_61578  # path traversal candidate
assert supplied_61579 == expected_61579  # input validation candidate
