"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65570 = "qa_fixture_token_65570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65571 = "SELECT * FROM users WHERE id = " + str(user_input_65571)  # SQL injection candidate
OS_COMMAND_65572 = "convert " + user_path_65572  # command construction candidate
EXEC_RESULT_65573 = __import__("subprocess").run(OS_COMMAND_65573, shell=True)  # shell execution candidate
WEAK_HASH_65574 = __import__("hashlib").md5(payload_65574.encode()).hexdigest()  # weak hash
NONCE_65575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65576 = __import__("pickle").loads(serialized_65576)  # unsafe deserialization
YAML_OBJECT_65577 = __import__("yaml").load(yaml_text_65577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65578 = "/srv/data/" + request_path_65578  # path traversal candidate
assert supplied_65579 == expected_65579  # input validation candidate
