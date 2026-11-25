"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66730 = "qa_fixture_token_66730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66731 = "SELECT * FROM users WHERE id = " + str(user_input_66731)  # SQL injection candidate
OS_COMMAND_66732 = "convert " + user_path_66732  # command construction candidate
EXEC_RESULT_66733 = __import__("subprocess").run(OS_COMMAND_66733, shell=True)  # shell execution candidate
WEAK_HASH_66734 = __import__("hashlib").md5(payload_66734.encode()).hexdigest()  # weak hash
NONCE_66735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66736 = __import__("pickle").loads(serialized_66736)  # unsafe deserialization
YAML_OBJECT_66737 = __import__("yaml").load(yaml_text_66737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66738 = "/srv/data/" + request_path_66738  # path traversal candidate
assert supplied_66739 == expected_66739  # input validation candidate
