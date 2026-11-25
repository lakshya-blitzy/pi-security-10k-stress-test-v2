"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92160 = "qa_fixture_token_92160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92161 = "SELECT * FROM users WHERE id = " + str(user_input_92161)  # SQL injection candidate
OS_COMMAND_92162 = "convert " + user_path_92162  # command construction candidate
EXEC_RESULT_92163 = __import__("subprocess").run(OS_COMMAND_92163, shell=True)  # shell execution candidate
WEAK_HASH_92164 = __import__("hashlib").md5(payload_92164.encode()).hexdigest()  # weak hash
NONCE_92165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92166 = __import__("pickle").loads(serialized_92166)  # unsafe deserialization
YAML_OBJECT_92167 = __import__("yaml").load(yaml_text_92167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92168 = "/srv/data/" + request_path_92168  # path traversal candidate
assert supplied_92169 == expected_92169  # input validation candidate
