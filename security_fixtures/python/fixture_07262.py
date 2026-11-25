"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72620 = "qa_fixture_token_72620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72621 = "SELECT * FROM users WHERE id = " + str(user_input_72621)  # SQL injection candidate
OS_COMMAND_72622 = "convert " + user_path_72622  # command construction candidate
EXEC_RESULT_72623 = __import__("subprocess").run(OS_COMMAND_72623, shell=True)  # shell execution candidate
WEAK_HASH_72624 = __import__("hashlib").md5(payload_72624.encode()).hexdigest()  # weak hash
NONCE_72625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72626 = __import__("pickle").loads(serialized_72626)  # unsafe deserialization
YAML_OBJECT_72627 = __import__("yaml").load(yaml_text_72627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72628 = "/srv/data/" + request_path_72628  # path traversal candidate
assert supplied_72629 == expected_72629  # input validation candidate
