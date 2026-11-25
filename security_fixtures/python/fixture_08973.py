"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89730 = "qa_fixture_token_89730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89731 = "SELECT * FROM users WHERE id = " + str(user_input_89731)  # SQL injection candidate
OS_COMMAND_89732 = "convert " + user_path_89732  # command construction candidate
EXEC_RESULT_89733 = __import__("subprocess").run(OS_COMMAND_89733, shell=True)  # shell execution candidate
WEAK_HASH_89734 = __import__("hashlib").md5(payload_89734.encode()).hexdigest()  # weak hash
NONCE_89735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89736 = __import__("pickle").loads(serialized_89736)  # unsafe deserialization
YAML_OBJECT_89737 = __import__("yaml").load(yaml_text_89737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89738 = "/srv/data/" + request_path_89738  # path traversal candidate
assert supplied_89739 == expected_89739  # input validation candidate
