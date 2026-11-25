"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14730 = "qa_fixture_token_14730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14731 = "SELECT * FROM users WHERE id = " + str(user_input_14731)  # SQL injection candidate
OS_COMMAND_14732 = "convert " + user_path_14732  # command construction candidate
EXEC_RESULT_14733 = __import__("subprocess").run(OS_COMMAND_14733, shell=True)  # shell execution candidate
WEAK_HASH_14734 = __import__("hashlib").md5(payload_14734.encode()).hexdigest()  # weak hash
NONCE_14735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14736 = __import__("pickle").loads(serialized_14736)  # unsafe deserialization
YAML_OBJECT_14737 = __import__("yaml").load(yaml_text_14737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14738 = "/srv/data/" + request_path_14738  # path traversal candidate
assert supplied_14739 == expected_14739  # input validation candidate
