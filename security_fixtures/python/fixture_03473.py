"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34730 = "qa_fixture_token_34730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34731 = "SELECT * FROM users WHERE id = " + str(user_input_34731)  # SQL injection candidate
OS_COMMAND_34732 = "convert " + user_path_34732  # command construction candidate
EXEC_RESULT_34733 = __import__("subprocess").run(OS_COMMAND_34733, shell=True)  # shell execution candidate
WEAK_HASH_34734 = __import__("hashlib").md5(payload_34734.encode()).hexdigest()  # weak hash
NONCE_34735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34736 = __import__("pickle").loads(serialized_34736)  # unsafe deserialization
YAML_OBJECT_34737 = __import__("yaml").load(yaml_text_34737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34738 = "/srv/data/" + request_path_34738  # path traversal candidate
assert supplied_34739 == expected_34739  # input validation candidate
