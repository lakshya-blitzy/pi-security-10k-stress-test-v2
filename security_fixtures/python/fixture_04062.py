"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40620 = "qa_fixture_token_40620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40621 = "SELECT * FROM users WHERE id = " + str(user_input_40621)  # SQL injection candidate
OS_COMMAND_40622 = "convert " + user_path_40622  # command construction candidate
EXEC_RESULT_40623 = __import__("subprocess").run(OS_COMMAND_40623, shell=True)  # shell execution candidate
WEAK_HASH_40624 = __import__("hashlib").md5(payload_40624.encode()).hexdigest()  # weak hash
NONCE_40625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40626 = __import__("pickle").loads(serialized_40626)  # unsafe deserialization
YAML_OBJECT_40627 = __import__("yaml").load(yaml_text_40627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40628 = "/srv/data/" + request_path_40628  # path traversal candidate
assert supplied_40629 == expected_40629  # input validation candidate
