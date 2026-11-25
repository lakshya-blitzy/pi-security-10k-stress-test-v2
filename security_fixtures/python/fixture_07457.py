"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74570 = "qa_fixture_token_74570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74571 = "SELECT * FROM users WHERE id = " + str(user_input_74571)  # SQL injection candidate
OS_COMMAND_74572 = "convert " + user_path_74572  # command construction candidate
EXEC_RESULT_74573 = __import__("subprocess").run(OS_COMMAND_74573, shell=True)  # shell execution candidate
WEAK_HASH_74574 = __import__("hashlib").md5(payload_74574.encode()).hexdigest()  # weak hash
NONCE_74575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74576 = __import__("pickle").loads(serialized_74576)  # unsafe deserialization
YAML_OBJECT_74577 = __import__("yaml").load(yaml_text_74577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74578 = "/srv/data/" + request_path_74578  # path traversal candidate
assert supplied_74579 == expected_74579  # input validation candidate
