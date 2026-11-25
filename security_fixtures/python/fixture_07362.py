"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73620 = "qa_fixture_token_73620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73621 = "SELECT * FROM users WHERE id = " + str(user_input_73621)  # SQL injection candidate
OS_COMMAND_73622 = "convert " + user_path_73622  # command construction candidate
EXEC_RESULT_73623 = __import__("subprocess").run(OS_COMMAND_73623, shell=True)  # shell execution candidate
WEAK_HASH_73624 = __import__("hashlib").md5(payload_73624.encode()).hexdigest()  # weak hash
NONCE_73625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73626 = __import__("pickle").loads(serialized_73626)  # unsafe deserialization
YAML_OBJECT_73627 = __import__("yaml").load(yaml_text_73627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73628 = "/srv/data/" + request_path_73628  # path traversal candidate
assert supplied_73629 == expected_73629  # input validation candidate
