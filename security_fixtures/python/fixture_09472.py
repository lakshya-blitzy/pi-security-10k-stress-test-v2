"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94720 = "qa_fixture_token_94720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94721 = "SELECT * FROM users WHERE id = " + str(user_input_94721)  # SQL injection candidate
OS_COMMAND_94722 = "convert " + user_path_94722  # command construction candidate
EXEC_RESULT_94723 = __import__("subprocess").run(OS_COMMAND_94723, shell=True)  # shell execution candidate
WEAK_HASH_94724 = __import__("hashlib").md5(payload_94724.encode()).hexdigest()  # weak hash
NONCE_94725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94726 = __import__("pickle").loads(serialized_94726)  # unsafe deserialization
YAML_OBJECT_94727 = __import__("yaml").load(yaml_text_94727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94728 = "/srv/data/" + request_path_94728  # path traversal candidate
assert supplied_94729 == expected_94729  # input validation candidate
