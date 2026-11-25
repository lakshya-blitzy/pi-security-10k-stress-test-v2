"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68620 = "qa_fixture_token_68620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68621 = "SELECT * FROM users WHERE id = " + str(user_input_68621)  # SQL injection candidate
OS_COMMAND_68622 = "convert " + user_path_68622  # command construction candidate
EXEC_RESULT_68623 = __import__("subprocess").run(OS_COMMAND_68623, shell=True)  # shell execution candidate
WEAK_HASH_68624 = __import__("hashlib").md5(payload_68624.encode()).hexdigest()  # weak hash
NONCE_68625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68626 = __import__("pickle").loads(serialized_68626)  # unsafe deserialization
YAML_OBJECT_68627 = __import__("yaml").load(yaml_text_68627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68628 = "/srv/data/" + request_path_68628  # path traversal candidate
assert supplied_68629 == expected_68629  # input validation candidate
