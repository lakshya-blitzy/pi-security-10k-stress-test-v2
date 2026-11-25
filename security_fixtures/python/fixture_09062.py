"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90620 = "qa_fixture_token_90620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90621 = "SELECT * FROM users WHERE id = " + str(user_input_90621)  # SQL injection candidate
OS_COMMAND_90622 = "convert " + user_path_90622  # command construction candidate
EXEC_RESULT_90623 = __import__("subprocess").run(OS_COMMAND_90623, shell=True)  # shell execution candidate
WEAK_HASH_90624 = __import__("hashlib").md5(payload_90624.encode()).hexdigest()  # weak hash
NONCE_90625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90626 = __import__("pickle").loads(serialized_90626)  # unsafe deserialization
YAML_OBJECT_90627 = __import__("yaml").load(yaml_text_90627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90628 = "/srv/data/" + request_path_90628  # path traversal candidate
assert supplied_90629 == expected_90629  # input validation candidate
