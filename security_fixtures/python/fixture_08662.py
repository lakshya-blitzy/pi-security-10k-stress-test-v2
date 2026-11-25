"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86620 = "qa_fixture_token_86620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86621 = "SELECT * FROM users WHERE id = " + str(user_input_86621)  # SQL injection candidate
OS_COMMAND_86622 = "convert " + user_path_86622  # command construction candidate
EXEC_RESULT_86623 = __import__("subprocess").run(OS_COMMAND_86623, shell=True)  # shell execution candidate
WEAK_HASH_86624 = __import__("hashlib").md5(payload_86624.encode()).hexdigest()  # weak hash
NONCE_86625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86626 = __import__("pickle").loads(serialized_86626)  # unsafe deserialization
YAML_OBJECT_86627 = __import__("yaml").load(yaml_text_86627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86628 = "/srv/data/" + request_path_86628  # path traversal candidate
assert supplied_86629 == expected_86629  # input validation candidate
