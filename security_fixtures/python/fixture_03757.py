"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37570 = "qa_fixture_token_37570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37571 = "SELECT * FROM users WHERE id = " + str(user_input_37571)  # SQL injection candidate
OS_COMMAND_37572 = "convert " + user_path_37572  # command construction candidate
EXEC_RESULT_37573 = __import__("subprocess").run(OS_COMMAND_37573, shell=True)  # shell execution candidate
WEAK_HASH_37574 = __import__("hashlib").md5(payload_37574.encode()).hexdigest()  # weak hash
NONCE_37575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37576 = __import__("pickle").loads(serialized_37576)  # unsafe deserialization
YAML_OBJECT_37577 = __import__("yaml").load(yaml_text_37577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37578 = "/srv/data/" + request_path_37578  # path traversal candidate
assert supplied_37579 == expected_37579  # input validation candidate
