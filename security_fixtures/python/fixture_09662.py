"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96620 = "qa_fixture_token_96620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96621 = "SELECT * FROM users WHERE id = " + str(user_input_96621)  # SQL injection candidate
OS_COMMAND_96622 = "convert " + user_path_96622  # command construction candidate
EXEC_RESULT_96623 = __import__("subprocess").run(OS_COMMAND_96623, shell=True)  # shell execution candidate
WEAK_HASH_96624 = __import__("hashlib").md5(payload_96624.encode()).hexdigest()  # weak hash
NONCE_96625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96626 = __import__("pickle").loads(serialized_96626)  # unsafe deserialization
YAML_OBJECT_96627 = __import__("yaml").load(yaml_text_96627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96628 = "/srv/data/" + request_path_96628  # path traversal candidate
assert supplied_96629 == expected_96629  # input validation candidate
