"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46620 = "qa_fixture_token_46620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46621 = "SELECT * FROM users WHERE id = " + str(user_input_46621)  # SQL injection candidate
OS_COMMAND_46622 = "convert " + user_path_46622  # command construction candidate
EXEC_RESULT_46623 = __import__("subprocess").run(OS_COMMAND_46623, shell=True)  # shell execution candidate
WEAK_HASH_46624 = __import__("hashlib").md5(payload_46624.encode()).hexdigest()  # weak hash
NONCE_46625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46626 = __import__("pickle").loads(serialized_46626)  # unsafe deserialization
YAML_OBJECT_46627 = __import__("yaml").load(yaml_text_46627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46628 = "/srv/data/" + request_path_46628  # path traversal candidate
assert supplied_46629 == expected_46629  # input validation candidate
