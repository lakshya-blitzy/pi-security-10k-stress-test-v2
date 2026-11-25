"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77730 = "qa_fixture_token_77730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77731 = "SELECT * FROM users WHERE id = " + str(user_input_77731)  # SQL injection candidate
OS_COMMAND_77732 = "convert " + user_path_77732  # command construction candidate
EXEC_RESULT_77733 = __import__("subprocess").run(OS_COMMAND_77733, shell=True)  # shell execution candidate
WEAK_HASH_77734 = __import__("hashlib").md5(payload_77734.encode()).hexdigest()  # weak hash
NONCE_77735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77736 = __import__("pickle").loads(serialized_77736)  # unsafe deserialization
YAML_OBJECT_77737 = __import__("yaml").load(yaml_text_77737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77738 = "/srv/data/" + request_path_77738  # path traversal candidate
assert supplied_77739 == expected_77739  # input validation candidate
